from rest_framework import serializers

from ..models import Cart, CartItem,WishList,WishListItems,OrderItem,Order
from apps.products.models import Product
from apps.accounts.models import CustomUser

from apps.accounts.api.serializers import CustomUserDetailsSerializer


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

class WishListItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishListItems
        fields = ['id','wishlist','item']
        depth = 1


class WishListSerializer(serializers.ModelSerializer):
    owner= CustomUserDetailsSerializer(many=False)
    owner = serializers.IntegerField(source='owner.id')

    # def validate(self, owner):
    #     abc = WishList.objects.filter(owner=owner).exists()
    #     if abc:
    #         raise serializers.ValidationError('Wishlist exists.Now add items')
    #     return owner

    def create(self, validated_data):
        user_data = validated_data.pop("owner")

        owner = CustomUser.objects.filter(**user_data).first()
        if owner is None:
            owner = CustomUser.objects.create(**user_data)
        validated_data.update({"owner": owner})
        return WishList.objects.create(**validated_data)

    class Meta:
        model = WishList
        fields = '__all__'
        depth = 1

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','user','ordered','item', 'quantity']
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'












