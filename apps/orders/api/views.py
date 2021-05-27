from rest_framework import response,status,mixins
# from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import as filterset
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
# import datetime
# import _datetime
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.http import Http404
from .serializers import *
from apps.products.models import *
from ..import models
from ..models import CartItem, Cart, WishList,WishListItems
from rest_framework.permissions import (AllowAny,IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListCreateAPIView,ListAPIView, UpdateAPIView,GenericAPIView,
RetrieveUpdateAPIView, RetrieveAPIView, GenericAPIView,)
from rest_framework.authtoken.models import Token
from django.db.models import Sum
from datetime import datetime, timedelta
from django.db.models import Count
from django.db.models import Q
from apps.accounts.models import CustomUser,Customer
from apps.accounts.api.serializers import *
from apps.products.api.pagination import CustomPagination
from rest_framework.filters import SearchFilter, OrderingFilter

class CartAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)


class CartwithItemAPIView(ListAPIView,mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartwithItemSerializer

    def get_queryset(self):
        return Cart.objects.filter(pk=self.kwargs['pk'])

    # def perform_update(self, serializer):
    #     user=Cart.objects.filter(pk=self.kwargs['pk'])
    #     serializer.save(owner=user)


class CartItemDetailAPIView(ListAPIView):
    permission_classes = [AllowAny]
    # queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(pk=self.kwargs['pk'])

class CartItemAPIView(ListCreateAPIView,mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        # user = self.request.user
        cart = get_object_or_404(Cart, pk=self.kwargs['pk1'])
        item = get_object_or_404(Product, pk=self.kwargs['pk2'])
        serializer.save(cart=cart,item=item)


class CartItemUpdateAPIView(UpdateAPIView,DestroyAPIView,):
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

 #WishLists endpoints start............................

        """
       WishLists endpoints start....................
        """

class WishListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WishList.objects.all()
    serializer_class = WishListItemsTestSerializer

    def perform_create(self, serializer):
        try:
            wishlist = WishList.objects.get(owner=self.request.user)
            return wishlist
            # return Response({"message": "Wishlist Already existed",
            #                  "wishlist": wishlist
            #                  },
            #                 status=status.HTTP_200_OK
            #                 )
        except ObjectDoesNotExist:
            user = self.request.user
            serializer.save(owner=user)
        # user = self.request.user
        # serializer.save(owner=user)



class WishListItemsAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WishListItems.objects.all()
    serializer_class = WishListItemsTestSerializer

    def perform_create(self, serializer):
        user = self.request.user
        #wishlist = get_object_or_404(WishList, pk=self.kwargs['pk1'])
        wishlist = WishList.objects.get(owner=user)
        item = get_object_or_404(Product, pk=self.kwargs['pk2'])
        serializer.save(wishlist=wishlist,item=item)

        """
            Updated WishLists endpoints start....................
               """

class AddtoWishListItemsView(CreateAPIView,DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WishListItems.objects.all()
    serializer_class = WishListItemsCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_seller:
            item = get_object_or_404(Product, pk=self.kwargs['pk1'])
            variants = get_object_or_404(Variants,pk=self.kwargs['pk2'])
            serializer.save(owner=user, item=item,wish_variants=variants)
        else:
            # return Response({

            #     "message":"This is not a customer account.Please login as customer.",},
            #     status = status.HTTP_200_OK
            # )
            raise serializers.ValidationError("This is not a customer account.Please login as customer.")

class DelWishListItemsView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WishListItems.objects.all()
    serializer_class = WishListItemsTestSerializer

    def perform_destroy(self, instance):
        instance.delete()

class WishListItemsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WishListItemsCreateSerializer

    def get_queryset(self):
        user = self.request.user
        return WishListItems.objects.filter(owner=user)



    """
       Orders endpoints start....................
    """

class AddtoOrderItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    # def post(self, request, pk):
    #     item = get_object_or_404(Product, pk=pk)
    #     order_item, created = OrderItem.objects.get_or_create(
    #         item=item,
    #         user=self.request.user,
    #         ordered=False
    #     )
    #     order_items = request.data.pop("order_items")
    #     order_qs = Order.objects.filter(user=self.request.user, ordered=False)
    #
    #     if order_qs.exists():
    #         order = order_qs[0]
    #     for order_item in order_items:
    #         if Product.objects.get(pk=order_item.item).exists():
    #             product = Product.objects.get(pk=order_item.item)
    #             item, created = OrderItem.objects.get_or_create(order=order, item=product)
    #             item.quantity = order_item.quantity
    #             item.save()

class OrderDetailView(ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        try:
            abc = Order.objects.filter(user=self.request.user)
            return abc
        except ObjectDoesNotExist:
            raise Http404("You do not have an active order")

class BillingInfoView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BillingDetails.objects.all()
    serializer_class = BillingInfoSerializer

class SellerOrderView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderDetailSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user__first_name','user__last_name','order_items_status' ]
    ordering_fields = ['order_items_price','ordered_date']
    pagination_class = CustomPagination

    def get_queryset(self):
        #return Order.objects.filter(item__merchant=self.kwargs['pk'])
        return Order.objects.filter(order_items__item__merchant=self.kwargs['pk'])




class DashboardView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        count_1 = Order.objects.filter(order_items__item__merchant=self.kwargs['pk']).count()
        count_2 = Token.objects.filter(user__is_customer=True).count()
        count_3 = Category.objects.count()
        count_4 = Variants.objects.filter(products__merchant=self.kwargs['pk']).count()
        count_5 = OrderItem.objects.filter(item__merchant=self.kwargs['pk']).aggregate(Sum('quantity'))
        count_6 = Subcategory.objects.count()
        count_7 = OrderItem.objects.filter(item__merchant=self.kwargs['pk']).aggregate(Sum('price'))


        count = []
        dates_count = []

        i=1
        while (i <= 31):
            startdate = datetime.today() - timedelta(days=i)
            enddate = startdate + timedelta(days=1)

            counts = Order.objects.filter(order_items__item__merchant=self.kwargs['pk'],
                                               ordered_date__range=[startdate, enddate]).count()

            count.append(counts)
            enddate = enddate.strftime('%m/%d/%Y')
            dates_count.append(enddate)
            i += 1

        dictionary = dict(zip(dates_count, count))

        #count_9 = Order.objects.annotate(abc=Count('user')).filter(order_items__item__merchant=self.kwargs['pk']).distinct().count()
        count_15 = Customer.objects.filter(customer__order__order_items__item__merchant=self.kwargs['pk']).distinct().count()

        return Response(
            {'active_users_now': count_2,
             'total_customers': count_15,
                'total_orders': count_1,
             'total_categories': count_3,
             'total_subcategories' : count_6,
             'total_products_available': count_4,
             'total_prodcuts_sold': count_5,
             'total_earnings': count_7,

             'orders_with_dates':dictionary

             },
            status=status.HTTP_200_OK)


class UpdateOrderView(UpdateAPIView,DestroyAPIView):
    permission_classes = [IsAuthenticated]
    #queryset = Order.objects.prefetch_related('order_items').all()
    #value = self.kwargs['pk']
    queryset = Order.objects.all()
    print(queryset)
    serializer_class = OrderUpdateSerializer



    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": "Order has been deleted successfully."
        },
            status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

class CustomersOfAMerchantView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerProfileSerializer
    pagination_class = CustomPagination
    search_fields = ['first_name', 'last_name', 'order_items_status']
    ordering_fields = ['ordered_date']

    def get_queryset(self):
        abc = Customer.objects.filter(customer__order__order_items__item__merchant=self.kwargs['pk']).distinct()
        #abc = Customer.objects.all()
        return abc





























