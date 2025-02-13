from datetime import datetime, timedelta

from django.shortcuts import render
from django.utils import timezone
from django.db import transaction

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, SAFE_METHODS

from .models import Card, Order
from .permission import IsAdminUserOrReadOnly
from .serializers import CardSerializer, OrderSerializer
from utils.errors import TradeError, response_data
from utils.common import get_random_code
from account.models import Profile
from utils.zhifubao import Alipay
from utils.filters import OrderFilter

# Create your views here.
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilter
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]
    
class AlipayAPIView(APIView):
    def get(self, request):
        card_id = request.GET.get('card_id', None)
        try:
            card = Card.objects.get(pk=card_id)
        except: 
            return Response(response_data(*TradeError.CardParamsError))

        out_trade_no = "pay" + datetime.now().strftime("%y%m%d%h%m%s") + get_random_code(4)
        
        #create order
        try: 
            Order.objects.create(
                profile = Profile.objects.get(user = request.user),
                card = card,
                order_sn = out_trade_no,
                order_amount = card.card_price,
                pay_time = timezone.now()
                
            )
        except: 
            return Response(response_data(*TradeError.OrderCreateError))
        
        # request payment 
        try: 
            alipay = Alipay()
            pay_url = alipay.trade_page(out_trade_no, str(card.card_price), card.card_name, 'alipay', 'FAST_INSTANT_TRADE_PAY')        
            return Response(pay_url)
        except: 
            return Response(response_data(*TradeError.PayRequestError))
        
class AlipayCallbackAPIView(APIView):
    def post(self, request):
        print("debugging line...")
        
        params = request.POST.dict()
        print("debugging line...")
        del params[sign_type]
        sorted_list = sorted([(k,v) for k,v in params.items()])
        unsigned_string = '&'.join(f"{k}={v}" for k,v in sorted_list)
        alipay = Alipay()
        print("debugging line...")
        if not alipay.verify_sign(unsigned_string, sign):
            print("verify sign error")
            return Response('error')
        try: 
            order = Order.objects.get(order_sn=params.get('out_trade_no'))
        except:
            print("cannot get out_trade_no")
            return Response('error')
        if params.get('total_amount') != str(order.order_amount):
            print('total amount is not same')
            return Response('error')
        if params.get('seller_id') != settings.ALIPAY_SELLER_ID:
            print('seller does not match')
            return Response('error')
        if params.get('app_id') != settings.ALIPAY_APP_ID:
            print('app id does not match')
            return Response('error')
        print('pass all verification')
        if params.get('trade_status') not in ['TRADE_SUCCESS', 'TRADE_FINISHED']:
            print('trade status does not match')
            return Response('error')
        # 
        print('pass all verification')
        # change table order
        with transaction.atomic():

            order.trade_no = params.get('trade_no')
            order.pay_status = params.get('trade_status')
            order.pay_time = timezone.now()
            order.save()

            # change table profile

            profile = Profile.objects.get(uid=order.profile.uid)
            profile.is_upgrade = 1
            profile.upgrade_time = timezone.now()
            profile.upgrade_count += 1
            # if the first time to upgrade or expire, duration is the current time + card duration
            # if membership card is not expired, duration should be the previous left time plus the new membership card duration
            if not profile.expire_time or profile.expire_time < timezone.now():
                profile.expire_time = profile.expire_time + timedelta(days=order.card.duration)
            else:
                profile.expire_time = timezone.now() + timedelta(days=order.card.duration)
            profile.save()
         
        return Response('success')
    

