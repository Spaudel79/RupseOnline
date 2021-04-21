from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import as filterset
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CustomPagination
from .filter import ProductFilter
from django.shortcuts import get_object_or_404
from .serializers import *
from .pagination import *
from ..import models
from ..models import Category, Brand, Collection, Product,Review,Banners
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAdminUser, IsAuthenticatedOrReadOnly)
from apps.accounts.models import Seller, Customer

from rest_framework.generics import (GenericAPIView,CreateAPIView, DestroyAPIView, ListCreateAPIView,ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView, mixins)


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

class PrdouctSearchAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    #search_fields = ['name','brand__name','brand__brand_category', 'description',
                     #'collection__name','category__name',]
    search_fields = ['name','brand__name','collection__name',
                     'category__name','description','variants__color']
    pagination_class = CustomPagination

class ProductDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_url_kwarg = 'slug'
    lookup_field = 'slug'

class CreateReviewAPIView(CreateAPIView,DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        user = self.request.user
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        serializer.save(user=user, product=product)

    # def get_queryset(self):
    #     product = get_object_or_404(Product, pk=self.kwargs['pk'])
    #     return Review.objects.filter(product=product)

    def perform_destroy(self, instance):
        instance.delete()



class GetReviewAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        user = self.request.user
        return Review.objects.filter(user=user)


    #MerchantAPis Starts Here

class SellerProductsAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        seller = get_object_or_404(Seller,pk=self.kwargs['pk'])
        return Product.objects.filter(merchant=seller)

class ProductAddAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer

    # def perform_create(self, serializer):
    #     brand = get_object_or_404(Brand, pk=self.kwargs['pk'])
    #     collection = get_object_or_404(Collection, pk=self.kwargs['pk'])
    #     serializer.save(brand=brand,collection=collection)


class ProductDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        instance.delete()

class ProductUpdateView(UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer

class VariantsUpdateDeleteView(DestroyAPIView,
                                UpdateAPIView,):
    permission_classes = [AllowAny]
    queryset = Variants.objects.all()
    serializer_class = VariantSerializer

    def perform_destroy(self, instance):
        instance.delete()


#Banners_endpoints

class BannersView(
                  mixins.ListModelMixin,GenericAPIView):
    permission_classes = [AllowAny]
    queryset = Banners.objects.all().order_by('-id')[:1]
    serializer_class = BannersSerializer

    # def list(self, request, *args, **kwargs):
    #     return (request,*args,**kwargs)


