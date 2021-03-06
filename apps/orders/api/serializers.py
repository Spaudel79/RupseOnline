from rest_framework import serializers

from apps.orders.models import Cart, CartItem,WishList,WishListItems,OrderItem,Order,BillingDetails,Coupons
from apps.products.models import Product,Variants
from apps.accounts.models import CustomUser
from django.db.models import F
from apps.accounts.api.serializers import CustomUserDetailsSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from apps.products.api.serializers import VariantSerializer,ProductSerializer

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
        fields = ['id','product_id','price','size','color','quantity','variant_availability']

class ProductSerializer(serializers.ModelSerializer):
    # variants = VariantSerializer(read_only=True)
    merchant = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'merchant',
            'category','brand','collection','sub_category','featured',
            'best_seller','top_rated','name','slug','main_product_image',
            'description','picture','rating',
            'availability','warranty',
            'services','variants'
        ]
        # lookup_field = "slug"
        #depth = 1

class WishListItemsCreateSerializer(serializers.ModelSerializer):
    # item = serializers.PrimaryKeyRelatedField(read_only=True)
    wish_variants = VariantSerializer(read_only=True)
    class Meta:
        model = WishListItems
        fields = ['id', 'item', 'wish_variants']
        #fields = '__all__'
        depth = 2



class WishListItemsTestSerializer(serializers.ModelSerializer):

    #wishlist = serializers.PrimaryKeyRelatedField(read_only=True,queryset=WishList.objects.filter(owner=serializers.CurrentUserDefault),default=serializers.CurrentUserDefault())
    class Meta:
        model = WishListItems
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    order = serializers.PrimaryKeyRelatedField(read_only=True)
    #price = serializers.FloatField(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['id','order','orderItem_ID','item','order_variants', 'quantity','order_item_status','price']
        # depth = 1

        # def get_price(self):
        #     return self. _price()

    #OrderItem.objects.annotate(total_item_price=F('quantity') * F('item.variants.price'))

class OrderItemUpdateSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField()
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['id','item','order','order_variants', 'quantity','order_item_status','price']
        # depth = 1


    # def update(self, instance, validated_data):
    #     order_items_data = validated_data.pop('')
    #
    #     for order_item_data in order_items_data:
    #         oi, created = OrderItem.objects.update_or_create(
    #             id = order_item_data['id'],
    #             defaults={
    #
    #                 'quantity' : order_item_data['quantity'],
    #                 'order_item_status': order_item_data['order_item_status']
    #
    #             }
    #         )

class BillingDetailsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    order = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = BillingDetails
        fields = ['id','user', 'order', 'first_name', 'last_name', 'email', 'phone', 'area',
                  'city', 'address', 'postal', 'payment_type' ]
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializer()
    order_items = OrderItemSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    #total_price = serializers.SerializerMethodField(source='get_total_price')
    #point_spent = serializers.FloatField(required=False)
    class Meta:
        model = Order
        fields = ['id','user','ordered_date','order_status', 'ordered', 'order_items','total_price','point_spent', 'billing_details']
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
            # breakpoint()
            # print(order_items)
            # print(validated_data)
            # print(**validated_data)
            billing_details = validated_data.pop('billing_details')
            order = Order.objects.create(user=user, **validated_data)
            BillingDetails.objects.create(user=user, order=order, **billing_details)
            for order_items in order_items:
                OrderItem.objects.create(order=order, **order_items)
            ordered = validated_data.get('ordered')
            order.ordered = True
            order.save()
            return order
        else:
            raise serializers.ValidationError("This is not a customer account.Please login as customer.")

    # def get_total_price(self):
    #     return sum([_.price for _ in self.order_items_set.all()])

class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    billing_details = BillingDetailsSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['id', 'user', 'ordered_date', 'order_status','ordered', 'order_items', 'total_price','point_spent','billing_details']
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
        fields = ['id', 'user', 'order', 'first_name','last_name','email','phone','area','city','address','postal']
        # depth = 1


    # def update(self, instance, validated_data):
    #     user = self.context['request'].user
    #     order_data = validated_data.pop('order')
    #     order = instance.order_data
    #     instance.billing_details = validated_data.get('billing_details', instance.order)
    #     billing_details = BillingDetails.objects.create(user=user,**validated_data)
    #     return billing_details


class OrderUpdateSerializer(serializers.ModelSerializer):
    order_items = OrderItemUpdateSerializer(many=True)
    billing_details = BillingDetailsSerializer()

    class Meta:
        model = Order
        fields = ['id','ordered','ordered_date','order_status','order_items','total_price','current_points','billing_details']
        depth= 2


    def update(self, instance, validated_data):
        # billing_details_data = validated_data.pop('billing_details', None)
        # order_items_data = validated_data.pop('order_items')

        #instance = super(OrderUpdateSerializer, self).update(instance,validated_data)
        #print(instance)
        instance.order_status = validated_data.get('order_status')
        instance.ordered = validated_data.get('ordered')

        #billing_details_logic

        billing_details_data = validated_data.pop('billing_details',None)
        if billing_details_data is not None:
            instance.billing_details.address = billing_details_data['address']
            instance.billing_details.save()


        #order_items_logic

        instance.save()

        #instance.order_items.clear()
        order_items_data = validated_data.pop('order_items')
        print(order_items_data)

        # for order_items_data in order_items_data:
        #     abc = OrderItem.objects.create(**order_items_data)
        #     instance.order_items.add(abc)
        
        for order_item_data in order_items_data:
            oi, created = OrderItem.objects.update_or_create(
                id = order_item_data['id'],

                defaults={
                    'quantity' : order_item_data['quantity'],
                    'order_item_status': order_item_data['order_item_status']
                }

            )
            #print(oi)
            # defaults = {
            #             'quantity' : order_item_data['quantity'],
            #             'order_item_status': order_item_data['order_item_status']
            #         }
            # try:
            #     oi = OrderItem.objects.get(id = order_item_data['id']
            #     for key, value in defaults.items():
            #         setattr(oi, key, value)
            #     oi.save()
            # except OrderItem.DoesNotExist:
            #     new_values = {}

            # print (oi)
            # instance.order_items.quantity = order_items_data['quantity']
            # instance.order_items.order_item_status = order_items_data['order_item_status']
            # instance.order_items.first().save()
            # msn = OrderItem.objects.create(**order_items_data)
            # instance.order_items.add(msn)
            #super(OrderUpdateSerializer, self).update(instance.order_items,validated_data).save()
        #super().save()
        #super().save()
        instance.save()
        super().update(instance,validated_data)
        return instance


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupons
        fields ='__all__'









