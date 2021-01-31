from rest_framework import serializers

from ..models import Product, Category, Brand, Collection


class CategorySerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ("id", "name","image")

class BrandSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = Brand
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = Collection
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # lookup_field = "slug"
        depth = 1

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category','brand', 'collection','featured', 'top_rated','name','description', 'picture',
                  'price', 'size', 'color','availability','warranty','services','quantity']
        # depth = 1