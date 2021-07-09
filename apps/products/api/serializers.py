from rest_framework import serializers
from ..models import Product, Category, Brand, Collection,Review,Variants,ImageBucket,Banners,Subcategory,Images
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Subcategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    subcategory = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ("id", "name","image",'subcategory')
        #fields = '__all__'

    def create(self, validated_data):
        name = validated_data.get('name')
        image = validated_data.get('image')
        category = Category.objects.create(name=name,image=image)

        category.save()

        subcategory_data = validated_data.get('subcategory')


        for subcategory_data in subcategory_data:
            abc = Subcategory.objects.create(**subcategory_data)
            category.subcategory.add(abc)

        category.save()
        return category






class BrandSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = Brand
        fields = ("id",'brand_category', "name", 'featured',"image")

    def create(self, validated_data):
        name = validated_data.get('name')
        featured = validated_data.get('featured')
        image = validated_data.get('image')

        brand = Brand.objects.create(name=name,featured=featured,image=image)


        brand_category_data = validated_data.get('brand_category')
        brand.brand_category.set(brand_category_data)
        brand.save()
        return brand

class CollectionSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = Collection
        # fields = ("id", "name","image")
        fields = '__all__'

class VariantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Variants
        fields = ['id','product_id','price','variant_image','size','color','quantity','variant_availability']

    def update(self, instance, validated_data):
         instance.product_id = validated_data.get('product_id',instance.product_id)
         instance.price = validated_data.get('price',instance.price)
         instance.variant_image = validated_data.get('variant_image',instance.variant_image)
         instance.size = validated_data.get('size', instance.size)
         instance.color = validated_data.get('color', instance.color)
         instance.quantity = validated_data.get('quantity', instance.quantity)
         instance.variant_availability = validated_data.get('variant_availability', instance.variant_availability)
         instance.save()
         return instance

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Review
        fields = ['id','user','product','user_rating','full_name','email','review','created_at']



class ProductSerializer(TaggitSerializer,serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    merchant = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = TagListSerializerField()
    category = CategorySerializer(many=True)
    #sub_category = SubCategorySerializer(many=True)
    class Meta:
        model = Product
        fields = ['id','merchant',
            'category','brand','collection','sub_category','featured',
            'best_seller','top_rated','name','slug','main_product_image','tags',
            'description','picture','rating',
            'availability','warranty',
            'services','variants','reviews'
        ]
        # lookup_field = "slug"
        depth = 1

class  SAddProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','merchant','featured', 'top_rated','category','brand','collection','sub_category',
                  'name','slug','description', 'main_product_image','best_seller','picture',
                  'rating','availability','warranty','services','variants']

class  AddProductSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    variants = VariantSerializer(many=True)
    slug = serializers.SlugField(read_only=True)
    # category = serializers.PrimaryKeyRelatedField(required=False,read_only=True)
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
        fields = ['id','merchant','featured', 'top_rated','category','brand','collection','sub_category',
                  'name','slug','description', 'main_product_image','best_seller','picture',
                  'rating','availability','warranty','services','variants']
        #depth = 1

    def create(self, validated_data):
         print(validated_data)
         #user = self.context['request'].user

         picture_data = validated_data.get('picture')

         merchant = validated_data.get('merchant')

         category_data = validated_data.get('category')
         print(category_data)

         featured = validated_data.get('featured')

         top_rated = validated_data.get('top_rated')
         brand = validated_data.get('brand')
         collection = validated_data.get('collection')
         sub_category = validated_data.get('sub_category')
         name = validated_data.get('name')
         description = validated_data.get('description')
         main_product_image = validated_data.get('main_product_image')
         best_seller = validated_data.get('best_seller')
         rating = validated_data.get('rating')
         availability = validated_data.get('availability')
         warranty = validated_data.get('warranty')
         services = validated_data.get('services')

         print(validated_data)
         #variants_logic


         variants_data = validated_data.get('variants')
         #breakpoint()
         # print(variants_data)


         # from pudb import set_trace;set_trace()

         #products-logic

         product = Product.objects.create(featured=featured,top_rated=top_rated,
                                          brand=brand,collection=collection,sub_category=sub_category,
                                          name=name,description=description,
                                          main_product_image=main_product_image,
                                          best_seller=best_seller,rating=rating,
                                          availability=availability,warranty=warranty,
                                          services=services,merchant=merchant)
         product.save()



         # for picture_data in picture_data:
         #    xyz = ImageBucket.objects.create(**picture_data)
         #    product.picture.add(xyz)



         # product.variants.set(variants_data)
         product.save()
         for variants_data in variants_data:
             abc = Variants.objects.create(**variants_data)
             product.variants.add(abc)

         product.save()
         return product


class ProductUpdateSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id','category','featured', 'top_rated','brand','collection',
                  'name','description', 'main_product_image','best_seller','picture',
                  'rating','availability','warranty','services','variants']

    def update(self, instance, validated_data):

        #instance = super(ProductUpdateSerializer, self).update(instance,validated_data)
        print(instance)
        instance.featured = validated_data.get('featured',instance.featured)
        instance.top_rated = validated_data.get('top_rated', instance.top_rated)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.collection = validated_data.get('collection',instance.collection)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.main_product_image = validated_data.get('main_product_image', instance.main_product_image)
        instance.best_seller = validated_data.get('best_seller',instance.best_seller)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.availability = validated_data.get('availability', instance.availability)
        instance.warranty = validated_data.get('warranty', instance.warranty)
        instance.services = validated_data.get('services', instance.services)

        instance.save()
        #
        #category_logic
        category_data = validated_data.pop('category')
        print(category_data)
        instance.category.set(category_data)
        instance.save()

        #picture_logic
        picture_data = validated_data.get('picture')
        #instance.variants.clear()
        for picture_data in picture_data:
            msn = ImageBucket.objects.create(**picture_data)
            instance.picture.add(msn)

        #variants_logic
        #instance.variants.clear()
        variants_data = validated_data.get('variants')
        print(variants_data)
        #instance.variants.set(variants_data)

        #variants_data.validated_data_set.all()
        # for variants_data in variants_data:
        #     abc = Variants.objects.create(**variants_data)
        #     instance.variants.add(abc)

        #variants_logic_trial

        for variants_data in variants_data:
             Variants.objects.update_or_create(
                id = variants_data['id'],
                defaults={

                    'price': variants_data['price'],
                    'size': variants_data['size'],
                    'color': variants_data['color'],
                    'quantity': variants_data['quantity'],
                    'variant_availability': variants_data['variant_availability'],
                }
            )




        #for variants_data in variants_data:
        # instance.variants.id = variants_data['id']
        # instance.variants__product_id = validated_data.get('product_id',instance.variants__product_id)
        # instance.abc = variants_data['price']
        # instance.variants.size = variants_data['size']
        # instance.variants.color = variants_data['color']
        # # instance.variants.variant_image = variants_data['variant_image']
        # instance.variants.quantity = variants_data['quantity']
        # instance.variants.variant_availability = variants_data['variant_availability']
        # # instance.variants.(variants_data)
        # instance.save()
        #category_data = instance.category
        #new_category = validated_data.pop('category')
        # for category_data in category_data:
        #     product = Product.objects.filter(category__id=category_data['id'])
        #     category = Category.objects.filter(id=category_data['id'])
        # for category_data in category_data:
        #     product.category.remove(category)
        #     product.category.add(category_data)

        instance.save()
        return instance






class Test(serializers.Serializer):
    pass

class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'