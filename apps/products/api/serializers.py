from rest_framework import serializers

from ..models import Product, Category, Brand, Collection,Review,Variants


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

class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variants
        fields = ['id','price','size','color','quantity','variant_availability']

class ProductSerializer(serializers.ModelSerializer):
    merchant = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ['id','merchant',
            'category','brand','collection','featured',
            'best_seller','top_rated','name','main_product_image',
            'description','picture','rating',
            'availability','warranty',
            'services','variants'
        ]
        # lookup_field = "slug"
        depth = 1

class  AddProductSerializer(serializers.ModelSerializer):
    #category = CategorySerializer(many=True,required=True)
    #brand = BrandSerializer(required=True)
    #collection = CollectionSerializer(required=True)
    merchant = serializers.PrimaryKeyRelatedField(read_only=True)
    #variants = VariantSerializer(many=True,required=True)

    # category = serializers.SlugRelatedField(
    #     many=True,
    #     queryset=Category.objects.all(),
    #     slug_field='name'
    # )
    # brand = serializers.SlugRelatedField(
    #     queryset=Brand.objects.all(),
    #     slug_field='name'
    # )
    # collection = serializers.SlugRelatedField(
    #     queryset=Collection.objects.all(),
    #     slug_field='name'
    # )
    class Meta:
        model = Product
        fields = ['merchant','featured', 'top_rated','category','brand','collection',
                  'name','description', 'picture','main_product_image','best_seller',
                  'rating','availability','warranty','services',]
        # depth = 1

    def create(self, validated_data):
         #user = self.context['request'].user
         category_data = validated_data.get('category')
         category_data = Category.objects.filter(category__id__in=category_data)
         product = Product.objects.create(**validated_data)
         product.category.set(category_data)
         # for abc in variants_data:
         #     #product.variants.set(['variants'])
         #     product.variants.add(abc)
         #product.variants.set(variants_data)



         return product



class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = ['id','user','product','user_rating','full_name','email','review','created_at']

class Test(serializers.Serializer):
    pass