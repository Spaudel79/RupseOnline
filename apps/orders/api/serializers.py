from rest_framework import serializers

from ..models import Cart, CartItem







class CartItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = CartItem
        fields = ['id','cart', 'item', 'quantity']
        depth = 1

class CartSerializer(serializers.ModelSerializer):
    cartitems = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        # fields = ("id", "name","image")
        fields = ['cartitems','owner','total_items','created_at','updated_at']
        depth = 1




