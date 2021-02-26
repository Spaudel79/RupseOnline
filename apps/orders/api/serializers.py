from rest_framework import serializers

from ..models import Cart, CartItem,WishList,WishListItems,OrderItem,Order,BillingDetails
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
    # owner= CustomUserDetailsSerializer(many=False)
    # owner = serializers.IntegerField(source='owner.id')

    # def validate(self, owner):
    #     abc = WishList.objects.filter(owner=owner["owner"]).exists()
    #     if abc:
    #         raise serializers.ValidationError('Wishlist exists.Now add items')
    #     return owner

    # def create(self, validated_data):
    #     user_data = validated_data.pop("owner")
    #
    #     owner = CustomUser.objects.filter(**user_data).first()
    #     if owner is None:
    #         owner = CustomUser.objects.create(**user_data)
    #     validated_data.update({"owner": owner})
    #     return WishList.objects.create(**validated_data)

    class Meta:
        model = WishList
        fields = '__all__'
        depth = 1

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','user','ordered','item', 'quantity']
        depth = 1

        # def save(self):
        #     instance = self.save(commit=False)
        #     instance.user = self.context['request'].user  # the request is added by default to the context
        #     instance.save()
        #     return instance

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        fields = ['id','user','start_date', 'ordered_date', 'ordered', 'order_items']
        # depth = 1

    # def save(self, **kwargs):
    #     instance = self.save(commit=False)
    #     instance.user = self.context['request'].user  # the request is added by default to the context
    #     instance.save()
    #     return instance

    def create(self, validated_data):
        # user = self.context['request'].user
        order_items = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for order_items in order_items:
            OrderItem.objects.create(order=order,**order_items)
        return order

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        depth = 1


class BillingDetailsSerializer(serializers.ModelSerializer):
    #order = OrderSerializer(many=True,required=False)

    class Meta:
        model = BillingDetails
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'country',
                  'city', 'address', 'postal',]
        depth = 1

    # def create(self, validated_data):
    #     order_data = validated_data.pop('order')
    #     bill = BillingDetails.objects.create(**validated_data)
    #     for order_data in order_data:
    #         Order.objects.create(billing_details=bill, **order_data)
    #     return bill











