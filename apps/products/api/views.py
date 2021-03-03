from rest_framework import viewsets
# from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import as filterset
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CustomPagination
from .filter import ProductFilter
from django.shortcuts import get_object_or_404
from .serializers import *
from .pagination import *
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
    pagination_class = CustomPagination

    # def get_queryset(self):
    #     brand = self.request.GET.get("brand", None)
    #     # collection = self.request.GET.get('collection', None)
    #     category = self.request.GET.get("category", None)
    #     if brand is not None:
    #         brand = self.request.GET.get("brand", "")
    #         brand_values = brand.split(",")
    #         if category is not None:
    #             category=self.request.GET.get("category","")
    #             category_values= category.split(",")
    #             return Product.objects.filter(brand__name__in=brand_values,category__name__in=category_values)
    #         else:
    #             return Product.objects.filter(brand__name__in=brand_values)
    #     elif category is not None:
    #         category = self.request.GET.get("category", "")
    #         category_values = category.split(",")
    #         if brand is not None:
    #             brand = self.request.GET.get("brand", "")
    #             brand_values = brand.split(",")
    #             return Product.objects.filter( category__name__in=category_values,brand__name__in=brand_values)
    #         else:
    #             return Product.objects.filter(category__name__in=category_values)
    #
    #     return Product.objects.all()

#Actual Filtering starts
    def get_queryset(self):
        brand = self.request.GET.get('brand',None)
        category = self.request.GET.get("category",None)
        warranty = self.request.GET.get("warranty", None)
        if brand is not None:
            brand = self.request.GET.get('brand', "")
            brand_values = brand.split(",")
            if category is not None:
                    category = self.request.GET.get("category", "")
                    category_values = category.split(",")
                    if warranty is not None:
                        warranty = self.request.GET.get("warranty", "")
                        warranty_values = warranty.split(",")
                        return Product.objects.filter(brand__name__in=brand_values,
                                              category__name__in=category_values,
                                                  warranty__in=warranty_values)
                    else:
                        return Product.objects.filter(brand__name__in=brand_values,
                                                  category__name__in=category_values,)
            elif warranty is not None:
                    warranty = self.request.GET.get("warranty", "")
                    warranty_values = warranty.split(",")
                    if category is not None:
                        category = self.request.GET.get("category", "")
                        category_values = category.split(",")
                        return Product.objects.filter(brand__name__in=brand_values,
                                                      category__name__in=category_values,
                                                      warranty__in=warranty_values)
                    else:
                        return Product.objects.filter(brand__name__in=brand_values,
                                                      warranty__in=warranty_values)
            else:
                    return Product.objects.filter(brand__name__in=brand_values,)

        elif category is not None:
            category = self.request.GET.get("category", "")
            category_values = category.split(",")
            if warranty is not None:
                warranty = self.request.GET.get("warranty", "")
                warranty_values = warranty.split(",")
                if brand is not None:
                    brand = self.request.GET.get('brand', "")
                    brand_values = brand.split(",")
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  category__name__in=category_values,
                                                  warranty__in=warranty_values)
                else:
                    return Product.objects.filter(category__name__in=category_values,
                                                  warranty__in=warranty_values)
            elif brand is not None:
                brand = self.request.GET.get('brand', "")
                brand_values = brand.split(",")
                if warranty is not None:
                    warranty = self.request.GET.get("warranty", "")
                    warranty_values = warranty.split(",")
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  category__name__in=category_values,
                                                  warranty__in=warranty_values)
                else:
                    return Product.objects.filter(category__name__in=category_values,
                                                  brand__name__in=brand_values,)
            else:
                return Product.objects.filter(category__name__in=category_values,)
        elif warranty is not None:
            warranty = self.request.GET.get("warranty", "")
            warranty_values = warranty.split(",")
            if brand is not None:
                brand = self.request.GET.get('brand', "")
                brand_values = brand.split(",")
                if category is not None:
                    category = self.request.GET.get("category", "")
                    category_values = category.split(",")
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  category__name__in=category_values,
                                                  warranty__in=warranty_values)
                else:
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  warranty__in=warranty_values)
            elif category is not None:
                category = self.request.GET.get("category", "")
                category_values = category.split(",")
                if brand is not None:
                    brand = self.request.GET.get('brand', "")
                    brand_values = brand.split(",")
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  category__name__in=category_values,
                                                  warranty__in=warranty_values)
                else:
                    return Product.objects.filter(category__name__in=category_values,
                                                  warranty__in=warranty_values)
            else:
                return Product.objects.filter(warranty__in=warranty_values)
        return Product.objects.all()

# Actual Filtering Ends

class ProductAddAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer

    # def perform_create(self, serializer):
    #     brand = get_object_or_404(Brand, pk=self.kwargs['pk'])
    #     collection = get_object_or_404(Collection, pk=self.kwargs['pk'])
    #     serializer.save(brand=brand,collection=collection)

class ProductDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer







