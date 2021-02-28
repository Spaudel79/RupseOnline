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
from apps.products.models import Product
from ..import models
from ..models import CartItem, Cart, WishList,WishListItems
from rest_framework.permissions import (AllowAny,IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListCreateAPIView,ListAPIView, UpdateAPIView,GenericAPIView,
RetrieveUpdateAPIView, RetrieveAPIView, GenericAPIView,)

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
    serializer_class = WishListSerializer

    def perform_create(self, serializer):
        try:
            wishlist = WishList.objects.get(owner=self.request.user)
            # return wishlist
            return Response({"message": "Wishlist Already existed",
                             "wishlist": wishlist
                             },
                            status=status.HTTP_200_OK
                            )
        except ObjectDoesNotExist:
            user = self.request.user
            serializer.save(owner=user)
        # user = self.request.user
        # serializer.save(owner=user)



class WishListItemsAPIView(ListCreateAPIView,mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = WishListItems.objects.all()
    serializer_class = WishListItemsSerializer

    def perform_create(self, serializer):
        # user = self.request.user
        wishlist = get_object_or_404(WishList, pk=self.kwargs['pk1'])
        item = get_object_or_404(Product, pk=self.kwargs['pk2'])
        serializer.save(wishlist=wishlist,item=item)


class OrderItemView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class AddressAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BillingDetails.objects.all()
    serializer_class = BillingDetailsSerializer

    def get_queryset(self):
        abc = BillingDetails.objects.filter(user=self.request.user)
        return abc

    # def perform_create(self, serializer):
    #     try:
    #         abc = BillingDetails.objects.(user=self.request.user)
    #         # return wishlist
    #         return Response({"message": "Wishlist Already existed",
    #                          "wishlist": abc
    #                          },
    #                         status=status.HTTP_200_OK
    #                         )
    #
    #     except ObjectDoesNotExist:
    #         user = self.request.user
    #         serializer.save(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class AddtoOrderView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BillingDetails.objects.all()
    serializer_class = BillingDetailsSerializer

    # def perform_create(self, serializer):

class AddtoOrderItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
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


class DelOrderItemView(DestroyAPIView,):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def perform_destroy(self, instance):
        instance.delete()

class OrderDetailView(ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (IsAuthenticated,)

    # def get_object(self):
    #     try:
    #         order = Order.objects.get(user=self.request.user, ordered=False)
    #         return order
    #     except ObjectDoesNotExist:
    #         raise Http404("You do not have an active order")

    def get_queryset(self):
        try:
            abc = Order.objects.filter(user=self.request.user)
            return abc
        except ObjectDoesNotExist:
            raise Http404("You do not have an active order")































