from rest_framework import generics
from django_filters import rest_framework as filters
from ..models import *


class ProductFilter(filters.FilterSet):
   price = filters.RangeFilter()

   class Meta:
      model = Product
      fields = ['price','availability',
                       'warranty', 'services','featured','best_seller','top_rated',
                'brand__id','category__id','collection__id','collection__name']


