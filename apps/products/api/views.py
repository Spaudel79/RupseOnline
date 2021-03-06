from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import as filterset
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from apps.products.api.utils import MultipartJsonParser

from .filter import ProductFilter
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import *
from .pagination import *
from ..import models
from ..models import Category, Brand, Collection, Product,Review,Banners,Images
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAdminUser, IsAuthenticatedOrReadOnly)
from apps.accounts.models import Seller, Customer

from rest_framework.generics import (GenericAPIView,CreateAPIView, DestroyAPIView, ListCreateAPIView,ListAPIView, UpdateAPIView,
RetrieveUpdateAPIView, RetrieveAPIView, mixins)
from rest_framework.parsers import FileUploadParser,FormParser,JSONParser,MultiPartParser




class CategoryAPIView(ListCreateAPIView):

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandAPIView(ListCreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand_category']

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class CollectionAPIView(ListCreateAPIView):

    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


# class ProductAPIView(ListAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = ProductSerializer
#     #queryset = Product.objects.all()
#
#     queryset = Product.objects.select_related('merchant','brand','collection','sub_category')
#     pagination_class = CustomPagination

class ProductAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['availability',
    #                     'warranty', 'services'
    #                     ]

    filterset_class = ProductFilter
    pagination_class = CustomPagination

    def get_queryset(self):
        brand = self.request.GET.get('brand', None)
        sub_category = self.request.GET.get("sub_category", None)
        warranty = self.request.GET.get("warranty", None)
        if brand is not None:
            brand = self.request.GET.get('brand', "")
            brand_values = brand.split(",")
            if sub_category is not None:
                sub_category = self.request.GET.get("sub_category", "")
                sub_category_values = sub_category.split(",")
                if warranty is not None:
                    warranty = self.request.GET.get("warranty", "")
                    warranty_values = warranty.split(",")
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  sub_category__name__in=sub_category_values,
                                                  warranty__in=warranty_values)
                else:
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  sub_category__name__in=sub_category_values, )
            elif warranty is not None:
                warranty = self.request.GET.get("warranty", "")
                warranty_values = warranty.split(",")
                if sub_category is not None:
                    sub_category = self.request.GET.get("sub_category", "")
                    sub_category_values = sub_category.split(",")
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  sub_category__name__in=sub_category_values,
                                                  warranty__in=warranty_values)
                else:
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  warranty__in=warranty_values)
            else:
                return Product.objects.filter(brand__name__in=brand_values, )

        elif sub_category is not None:
            sub_category = self.request.GET.get("sub_category", "")
            sub_category_values = sub_category.split(",")
            if warranty is not None:
                warranty = self.request.GET.get("warranty", "")
                warranty_values = warranty.split(",")
                if brand is not None:
                    brand = self.request.GET.get('brand', "")
                    brand_values = brand.split(",")
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  sub_category__name__in=sub_category_values,
                                                  warranty__in=warranty_values)
                else:
                    return Product.objects.filter(sub_category__name__in=sub_category_values,
                                                  warranty__in=warranty_values)
            elif brand is not None:
                brand = self.request.GET.get('brand', "")
                brand_values = brand.split(",")
                if warranty is not None:
                    warranty = self.request.GET.get("warranty", "")
                    warranty_values = warranty.split(",")
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  sub_category__name__in=sub_category_values,
                                                  warranty__in=warranty_values)
                else:
                    return Product.objects.filter(sub_category__name__in=sub_category_values,
                                                  brand__name__in=brand_values, )
            else:
                return Product.objects.filter(sub_category__name__in=sub_category_values, )
        elif warranty is not None:
            warranty = self.request.GET.get("warranty", "")
            warranty_values = warranty.split(",")
            if brand is not None:
                brand = self.request.GET.get('brand', "")
                brand_values = brand.split(",")
                if sub_category is not None:
                    sub_category = self.request.GET.get("sub_category", "")
                    sub_category_values = sub_category.split(",")
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  sub_category__name__in=sub_category_values,
                                                  warranty__in=warranty_values)
                else:
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  warranty__in=warranty_values)
            elif sub_category is not None:
                sub_category = self.request.GET.get("sub_category", "")
                sub_category_values = sub_category.split(",")
                if brand is not None:
                    brand = self.request.GET.get('brand', "")
                    brand_values = brand.split(",")
                    return Product.objects.filter(brand__name__in=brand_values,
                                                  sub_category__name__in=sub_category_values,
                                                  warranty__in=warranty_values)
                else:
                    return Product.objects.filter(sub_category__name__in=sub_category_values,
                                                  warranty__in=warranty_values)
            else:
                return Product.objects.filter(warranty__in=warranty_values)
        return Product.objects.all()

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


# Actual Filtering Ends

from django.db.models import Q
class PrdouctSearchAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination

    # def list(self, request, *args, **kwargs):
    # def get(self, request, *args, **kwargs):
    def get_queryset(self):
        qur = self.request.query_params.get('search')
        if qur == 'tv' or qur == 'Tv' or qur == 'TV':
            item = Product.objects.filter(Q(name__icontains=qur))
        else:
            item = Product.objects.filter(Q(category__name__icontains=qur) |
                                          Q(brand__name__icontains=qur) |
                                          Q(description__icontains=qur) |
                                          Q(collection__name__icontains=qur) |
                                          Q(name__icontains=qur) |
                                          Q(variants__color__icontains=qur)).distinct()

        return item
        # serializer = ProductSerializer(item,many=True)
        # return Response(serializer.data)

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
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name',]
    ordering_fields = ['variants__price','name']
    pagination_class = CustomPagination

    def get_queryset(self):
        seller = get_object_or_404(Seller,pk=self.kwargs['pk'])
        return Product.objects.filter(merchant=seller)

class SProductAddAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser,JSONParser,FormParser]
    # queryset = Product.objects.all()
    # parser_classes = [MultipartJsonParser,JSONParser]
    serializer_class = AddProductSerializer

    # def perform_create(self, serializer):
    #     brand = get_object_or_404(Brand, pk=self.kwargs['pk'])
    #     collection = get_object_or_404(Collection, pk=self.kwargs['pk'])
    #     serializer.save(brand=brand,collection=collection)

import json
class ProductAddAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultipartJsonParser, JSONParser]

    def post(self,request,*args,**kwargs):
        data = request.data
        print(request.data['category'])
        serializer = AddProductSerializer(data=data)
        # print(serializer)
        if serializer.is_valid():
            return Response(serializer.data,
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class VarinatAddAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Variants.objects.all()
    print(queryset)
    serializer_class = VariantSerializer


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
                  ListAPIView):
    permission_classes = [AllowAny]
    queryset = Banners.objects.all().order_by('-id')[:1]
    serializer_class = BannersSerializer


class ImageView(ListCreateAPIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser,FileUploadParser]
    queryset = Images.objects.all().order_by('-id')[:1]
    serializer_class = ImageSerializer




