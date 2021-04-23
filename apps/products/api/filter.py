from rest_framework import generics
from django_filters import rest_framework as filters
from ..models import *


class ProductFilter(filters.FilterSet):
   variants__price = filters.RangeFilter()

   class Meta:
      model = Product
      fields = ['variants__price','availability','slug','sub_category',
                       'services','featured','best_seller','top_rated',
                'brand__id','category__id','collection__id','collection__name']


