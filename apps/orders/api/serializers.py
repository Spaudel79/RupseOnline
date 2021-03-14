from rest_framework import serializers

from ..models import Cart, CartItem,WishList,WishListItems,OrderItem,Order,BillingDetails
from apps.products.models import Product,Variants
from apps.accounts.models import CustomUser

from apps.accounts.api.serializers import CustomUserDetailsSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from apps.products.api.serializers import VariantSerializer

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

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variants
        fields = ['id','product_id','price','size','color','quantity','vairant_availability']

class WishListItemsCreateSerializer(serializers.ModelSerializer):
    # item = serializers.PrimaryKeyRelatedField(read_only=True)
    wish_variants = VariantSerializer(read_only=True)
    class Meta:
        model = WishListItems
        fields = ['id', 'item', 'wish_variants']
        #fields = '__all__'
        depth = 1



class WishListItemsTestSerializer(serializers.ModelSerializer):

    #wishlist = serializers.PrimaryKeyRelatedField(read_only=True,queryset=WishList.objects.filter(owner=serializers.CurrentUserDefault),default=serializers.CurrentUserDefault())
    class Meta:
        model = WishListItems
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    #order_variants = VariantSerializer(read_only=True)
    #order_variants =VariantSerializer()
    class Meta:
        model = OrderItem
        fields = ['id','order','item','order_variants', 'quantity']
        # depth = 1


class BillingDetailsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = BillingDetails
        fields = ['id','user', 'order', 'first_name', 'last_name', 'email', 'phone', 'country',
                  'city', 'address', 'postal', 'payment_type' ]
        depth = 1

class OrderSerializer(serializers.ModelSerializer):

    billing_details = BillingDetailsSerializer()
    order_items = OrderItemSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        fields = ['id','user','ordered_date', 'ordered', 'order_items','billing_details']
        # depth = 1

    # def save(self, **kwargs):
    #     instance = self.save(commit=False)
    #     instance.user = self.context['request'].user  # the request is added by default to the context
    #     instance.save()
    #     return instance

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     order_items = validated_data.pop('order_items')
    #     order = Order.objects.create(user=user,**validated_data)
    #     for order_items in order_items:
    #         OrderItem.objects.create(order=order,**order_items)
    #     return order

    def create(self, validated_data):
        user = self.context['request'].user
        if not user.is_seller:
            order_items = validated_data.pop('order_items')
            billing_details = validated_data.pop('billing_details')
            order = Order.objects.create(user=user,**validated_data)
            BillingDetails.objects.create(user=user,order=order,**billing_details)
            for order_items in order_items:
                OrderItem.objects.create(order=order,**order_items)
            # return Response ({"order": order,
            #                     "billing_details":billing_details
            #                      },
            #                     status=status.HTTP_201_CREATED
            #                     )
            return order
        else:
            raise serializers.ValidationError("This is not a customer account.Please login as customer.")

class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    billing_details = BillingDetailsSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['id', 'user','ordered_date', 'ordered', 'order_items','billing_details']
        depth = 1

class OrderBillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'start_date', 'ordered_date', 'ordered', 'order_items',]


class BillingInfoSerializer(serializers.ModelSerializer):
    order = OrderDetailSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = BillingDetails
        fields = ['id', 'user', 'order', 'first_name','last_name','email','phone','country','city','address','postal']
        # depth = 1


    # def update(self, instance, validated_data):
    #     user = self.context['request'].user
    #     order_data = validated_data.pop('order')
    #     order = instance.order_data
    #     instance.billing_details = validated_data.get('billing_details', instance.order)
    #     billing_details = BillingDetails.objects.create(user=user,**validated_data)
    #     return billing_details










