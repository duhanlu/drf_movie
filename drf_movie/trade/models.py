from django.db import models

from account.models import Profile

# Create your models here.
class Card(models.Model):
    card_name = models.CharField("membership name", max_length=100, unique=True)
    card_price = models.DecimalField("price", max_digits=8, decimal_places=2)
    duration = models.IntegerField("duration")
    info = models.CharField("membership info", max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=True, verbose_name="create time")
    updated_at = models.DateTimeField(auto_now=True, editable=True, verbose_name="update time")
    
    class Meta:
        db_table = 'card'
        verbose_name = "card info"
        verbose_name_plural = verbose_name

class Order(models.Model):
    
    ORDER_STATUS = {
        ("TRADE_SUCCESS", 'trade success'),
        ("TRADE_CLOSED", "trade closed"),
        ("WAIT_BUYER_PAY", "trade created"),
        ("TRADE_FINISHED", "trade finished"),
        ("PAYING", "wait for payment")
    }
    
    PAY_TYPE = {
        ("alipay", "alipay"),
        ("wechat", "wechat"),
    }
    profile = models.ForeignKey(Profile, related_name='orders', to_field='uid', on_delete=models.CASCADE, verbose_name='profile')
    card = models.ForeignKey(Card, related_name='+', on_delete=models.DO_NOTHING, verbose_name='membership card')
    order_sn = models.CharField('order number', max_length=30, null=True, blank=True, unique=True)
    trade_no = models.CharField('trade number', max_length=100, unique=True, null=True, blank=True)
    pay_status = models.CharField('order status', choices=ORDER_STATUS, default='PAYING', max_length=30)
    pay_type = models.CharField('payment type', choices=PAY_TYPE, default='alipay', max_length=10)
    order_amount = models.DecimalField('order amount', max_digits=10, decimal_places=2)
    pay_time = models.DateTimeField('payment time', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=True, verbose_name='create time')
    updated_at = models.DateTimeField(auto_now=True, editable=True, verbose_name='update time')
    
    class Meta: 
        db_table = 'order'
        verbose_name = 'order info'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return str(self.order_sn)