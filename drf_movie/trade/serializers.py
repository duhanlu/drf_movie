from rest_framework import serializers 

from .models import Card, Order
class CardSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Card
        fields = "__all__"
        
class OrderSerializer(serializers.ModelSerializer):
    card = CardSerializer()
    
    class Meta: 
        model = Order
        fields = ['order_sn', 'pay_status', 'order_amount', 'created_at', 'card']