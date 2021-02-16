from rest_framework import serializers

from ..models import Product, Category, Brand, Collection


class CategorySerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = Category
        # fields = ("id", "name","image")
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = Brand
        fields = '__all__'
        # fields = ("id", "name", "image")

class CollectionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = Collection
        # fields = ("id", "name","image")
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id',
            'category','brand','collection','featured',
            'best_seller','top_rated','name',
            'description','picture','price','size',
            'color','quantity','availability','warranty',
            'services',
        ]
        # lookup_field = "slug"
        depth = 1

class  AddProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        queryset=Category.objects.all(),
        slug_field='name'
    )
    brand = serializers.SlugRelatedField(
        queryset=Brand.objects.all(),
        slug_field='name'
    )
    collection = serializers.SlugRelatedField(
        queryset=Collection.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Product
        fields = ['category','brand', 'collection','featured', 'top_rated','name','description', 'picture',
                  'price', 'size', 'color','availability','warranty','services','quantity']
        # depth = 1