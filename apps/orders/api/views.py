from rest_framework import viewsets
# from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import as filterset
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import get_object_or_404
from .serializers import *
from apps.products.models import Product
from ..import models
from ..models import CartItem, Cart
from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)

from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListCreateAPIView,ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView)

class CartAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemDetailAPIView(ListAPIView):
    permission_classes = [AllowAny]
    # queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(pk=self.kwargs['pk'])

class CartItemAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        # user = self.request.user
        cart = get_object_or_404(Cart, pk=self.kwargs['pk1'])
        item = get_object_or_404(Product, pk=self.kwargs['pk2'])
        serializer.save(cart=cart,item=item)












