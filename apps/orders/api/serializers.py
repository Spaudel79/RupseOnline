from rest_framework import serializers

from ..models import Cart, CartItem,WishList





class CartItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = CartItem
        fields = ['id','cart', 'item', 'quantity']
        depth = 1

class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        # fields = ("id", "name","image")
        fields = '__all__'
        # depth = 1

class CartwithItemSerializer(serializers.ModelSerializer):
    cartitems = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        # fields = ("id", "name","image")
        fields = ['id','cartitems']
        # depth = 1

        """
               WishLists serializers start....................
        """

class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishList
        fields = '__all__'
        depth = 1








