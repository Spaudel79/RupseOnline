from rest_framework import viewsets
# from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import as filterset
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProductFilter
from django.shortcuts import get_object_or_404
from .serializers import *
from ..import models
from ..models import Category, Brand, Collection, Product
from rest_framework.permissions import (AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly)

from rest_framework.generics import (CreateAPIView, DestroyAPIView, ListCreateAPIView,ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView)

# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     # permission_classes = [permissions.IsAuthenticated, ]
#     serializer_class = ProductSerializer
#     lookup_field = "slug"
#
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ["category__name", "name", "description"]

class CategoryAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CollectionAPIView(ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

class ProductAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['availability',
    #                     'warranty', 'services'
    #                     ]
    filterset_class = ProductFilter

    def get_queryset(self):
        brand = self.request.query_params.get('brand', None)
        collection = self.request.query_params.get('collection', None)
        category = self.request.query_params.get('category', None)
        if brand is not None:
            if collection is not None:
                if category is not None:
                    return Product.objects.filter(brand__name=brand, collection__name=collection, category__name=category)
                else:
                    return Product.objects.filter(brand__name=brand, collection__name=collection)
            else:
                return Product.objects.filter(brand__name=brand)

        elif collection is not None:
            if category is not None:
                if brand is not None:
                    return Product.objects.filter(brand__name=brand, collection__name=collection, category__name=category)
                else:
                    return Product.objects.filter(collection__name=collection, category__name=category)
            else:
                return Product.objects.filter(collection__name=collection)
        elif category is not None:
            if brand is not None:
                if collection is not None:
                    return Product.objects.filter(brand__name=brand, collection__name=collection,
                                                  category__name=category)
                else:
                    return Product.objects.filter(brand__name=brand,category__name=category)
            else:
                return Product.objects.filter(brand__name=brand)

        else:
            return Product.objects.all()


class ProductAddAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer

    # def perform_create(self, serializer):
    #     # user = self.request.user
    #     category = get_object_or_404(Package, pk=self.kwargs['pk'])
    #     serializer.save(user=self.request.user, package=package)









