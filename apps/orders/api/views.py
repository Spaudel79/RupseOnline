from rest_framework import response,status,mixins
# from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import as filterset
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
import datetime
from django.shortcuts import get_object_or_404
from .serializers import *
from apps.products.models import Product
from ..import models
from ..models import CartItem, Cart, WishList,WishListItems
from rest_framework.permissions import (AllowAny,IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListCreateAPIView,ListAPIView, UpdateAPIView,GenericAPIView,
RetrieveUpdateAPIView, RetrieveAPIView, GenericAPIView)

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

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(owner=user)



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

class AddtoOrderItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    #@action(detail=True, methods=['post'])
    def add_to_order(request, pk):
        item = get_object_or_404(Product, pk=pk)
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False
        )
        order_qs = Order.objects.filter(user=request.user, ordered=False)

        if order_qs.exists():
            order = order_qs[0]

            if order.items.filter(item__pk=item.pk).exists():
                order_item.quantity += 1
                order_item.save()
                # messages.info(request, "Added quantity Item")
                # return redirect("core:product", pk=pk)
                return Response({"message":"Added quantity Item",},
                                 status=status.HTTP_201_CREATED,
                )
            else:
                order.items.add(order_item)
                #messages.info(request, "Item added to your cart")
                # return redirect("core:product", pk=pk)
                return Response({"message": " Item added to your cart", },
                                status=status.HTTP_201_CREATED,
                                )
        else:
            ordered_date = datetime.timezone.now()
            order = Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.items.add(order_item)
            #messages.info(request, "Item added to your cart")
            # return redirect("core:product", pk=pk)
            return Response({"message": "Item added to your cart", },
                            status=status.HTTP_201_CREATED,
                            )


































