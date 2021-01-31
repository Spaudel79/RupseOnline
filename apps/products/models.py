from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(null=True, blank=True)


    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:category", kwargs={"name": self.name})


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
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
    SIZE = (
        ('not applicable', 'not applicable',),
        ('S', 'Small',),
        ('M', 'Medium',),
        ('L', 'Large',),
        ('XL', 'Extra Large',),
    )
    category = models.ManyToManyField(Category, blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)  # is product featured?
    best_seller = models.BooleanField(default=False)
    top_rated = models.BooleanField(default=False)
    tags = TaggableManager(blank=True)  # tags mechanism
    name = models.CharField(max_length=150)
    # slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=500, default="Empty description.")
    picture = models.ImageField(upload_to="products/images", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    size = models.CharField(max_length=50, choices=SIZE, default='not applicable')
    color = models.CharField(max_length=70, default="not applicable")
    quantity = models.IntegerField(default=10)  # available quantity of given product
    availability = models.CharField(max_length=70, choices=AVAILABILITY, default='in_stock')
    warranty = models.CharField(max_length=100, choices=WARRANTY, default='no_warranty')
    services = models.CharField(max_length=100, choices=SERVICES, default='cash_on_delivery')



    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    @property
    def is_featured(self):
        return self.featured

    @property
    def is_available(self):
        return self.quantity > 0
