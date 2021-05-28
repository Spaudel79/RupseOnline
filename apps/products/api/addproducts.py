class  AddProductSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    variants = VariantSerializer(many=True,required=False)
    slug = serializers.SlugField(read_only=True)
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
         #user = self.context['request'].user
         picture_data = validated_data.get('picture')
         merchant = validated_data.get('merchant')
         category_data = validated_data.get('category')
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

        #variants_logic

         variants_data = validated_data.get('variants')


         #products-logic

         product = Product.objects.create(featured=featured,top_rated=top_rated,
                                          brand=brand,collection=collection,sub_category=sub_category,
                                          name=name,description=description,
                                          main_product_image=main_product_image,
                                          best_seller=best_seller,rating=rating,
                                          availability=availability,warranty=warranty,
                                          services=services,merchant=merchant)
         product.save()
         #category_data = Category.objects.filter(category__in=category_data)

         product.category.set(category_data)
         for picture_data in picture_data:
            xyz = ImageBucket.objects.create(**picture_data)
            product.picture.add(xyz)

         product.save()
         for variants_data in variants_data:
             abc = Variants.objects.create(**variants_data)
             product.variants.add(abc)
         # for abc in variants_data:
         #     #product.variants.set(['variants'])
         #     product.variants.add(abc)
         #product.variants.set(variants_data)
         product.save()
         return product


    #variants_data

    {
        "product_id": "OAXWRTZ_12C",
        "price": "500.00",
        "size": "not applicable",
        "color": "not applicable",
        "variant_image": null,
        "quantity": 10,
        "variant_availability": "available"
    },
    {
        "product_id": "OGROUPIRZ_12C",
        "price": "888.00",
        "size": "not applicable",
        "color": "not applicable",
        "variant_image": null,
        "quantity": 10,
        "variant_availability": "available"
    }