from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from apps.accounts.models import Seller
from django.utils.text import slugify
# Create your models here.
User = get_user_model()

class Category(models.Model):
    #parent = models.ForeignKey('self',related_name='children',on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(null=True, blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        #return reverse("products:category", kwargs={"name": self.name})

class Subcategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True,related_name='subcategory')
    name =  models.CharField(max_length=100, unique=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Sub Category"

    def __str__(self):
        return self.name

class Brand(models.Model):
    brand_category = models.ManyToManyField(Category,blank=True,null=True)
    name = models.CharField(max_length=100, unique=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Collections"

    def __str__(self):
        return self.name

class ImageBucket(models.Model):
    pic_name = models.CharField(max_length=100,blank=True)
    pic = models.ImageField(upload_to="products/images", null=True, blank=True)
    thumbnail = ImageSpecField(source='pic',
                               processors=[ResizeToFill(100, 50)],
                               format='JPEG',
                               options={'quality': 60})

    def __str__(self):
        return self.pic_name

    class Meta:
        verbose_name_plural = "Image Gallery"


class Variants(models.Model):
    SIZE = (
        ('not applicable', 'not applicable',),
        ('S', 'Small',),
        ('M', 'Medium',),
        ('L', 'Large',),
        ('XL', 'Extra Large',),
    )
    AVAILABILITY = (
        ('available', 'Available',),
        ('not_available', 'Not Available',),
    )
    product_id = models.CharField(max_length=70, default='OAXWRTZ_12C',blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20,default=500)
    size = models.CharField(max_length=50, choices=SIZE, default='not applicable',blank=True,null=True)
    color = models.CharField(max_length=70, default="not applicable",blank=True,null=True)
    variant_image = models.ImageField(upload_to="products/images", blank=True)
    thumbnail = ImageSpecField(source='variant_image',
                               processors=[ResizeToFill(100, 50)],
                               format='JPEG',
                               options={'quality': 60})
    quantity = models.IntegerField(default=10,blank=True,null=True)  # available quantity of given product
    variant_availability = models.CharField(max_length=70, choices=AVAILABILITY, default='available')

    class Meta:
        verbose_name_plural = "Variants"

    def __str__(self):
        return self.product_id

class Product(models.Model):
    AVAILABILITY = (
        ('in_stock', 'In Stock',),
        ('not_available', 'Not Available',),
        )
    WARRANTY = (
        ('no_warranty', 'No Warranty',),
        ('local_seller_warranty', 'Local Seller Warranty',),
        ('brand_warranty', 'Brand Warranty',),
    )
    SERVICES = (
        ('cash_on_delivery', 'Cash On Delivery',),
        ('free_shipping', 'Free Shipping',),
    )
    merchant = models.ForeignKey(Seller,on_delete=models.CASCADE,blank=True,null=True)
    category = models.ManyToManyField(Category, blank=False)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE,blank=True,null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)  # is product featured?
    best_seller = models.BooleanField(default=False)
    top_rated = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)  # tags mechanism
    name = models.CharField(max_length=150,unique=True)
    main_product_image = models.ImageField(upload_to="products/images", null=True, blank=True)
    thumbnail = ImageSpecField(source='main_product_image',
                               processors=[ResizeToFill(100, 50)],
                               format='JPEG',
                               options={'quality': 60})
    slug = models.SlugField(max_length=200,blank=True)
    # description = models.TextField(max_length=500, default="Empty description.")
    description = RichTextField(blank=True)
    #picture = models.ImageField(upload_to="products/images", null=True, blank=True)
    picture = models.ManyToManyField(ImageBucket,null=True,blank=True,verbose_name="Add extra 3 images")
    rating = models.IntegerField(choices=((1, 1),
                                               (2, 2),
                                               (3, 3),
                                               (4, 4),
                                               (5, 5))
                                      )
    availability = models.CharField(max_length=70, choices=AVAILABILITY, default='in_stock')
    warranty = models.CharField(max_length=100, choices=WARRANTY, default='no_warranty')
    services = models.CharField(max_length=100, choices=SERVICES, default='cash_on_delivery')
    variants = models.ManyToManyField(Variants,related_name='products')


    class Meta:
        ordering = ("-id" ,)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
    # @property
    # def get_price(self):
    #     return self.variants.price

    @property
    def is_featured(self):
        return self.featured

    @property
    def is_available(self):
        return self.quantity > 0

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user_rating = models.IntegerField(choices=((1, 1),
                                          (2, 2),
                                          (3, 3),
                                          (4, 4),
                                          (5, 5))
                                 )
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    review = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ('created_at',)

class Banners(models.Model):
    banner_image_1 = models.ImageField(upload_to="banners/images", blank=True)
    banner_image_2 = models.ImageField(upload_to="banners/images", blank=True)
    banner_image_3 = models.ImageField(upload_to="banners/images", blank=True)
    square_image_1 = models.ImageField(upload_to="banners/images", blank=True)
    square_image_2 = models.ImageField(upload_to="banners/images", blank=True)
    square_image_3 = models.ImageField(upload_to="banners/images", blank=True)

    class Meta:
        verbose_name_plural = 'Banner Images'


