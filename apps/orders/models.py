from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product, Variants
from django.db.models.signals import post_save
from decimal import *

# import settings
from django.utils.crypto import get_random_string
#from python_utils import *
#from utils import create_new_ref_number
import uuid
import random
import string
# Create your models here.

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

User = get_user_model()

class Cart(models.Model):

    owner = models.OneToOneField(User,on_delete=models.CASCADE, null=True,blank=True)
    total_items = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User: {self.owner}, items in cart {self.total_items}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, related_name='cartitems')
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item.name


class WishList(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # item = models.ManyToManyField(Product,blank=True, null=True)

    def __str__(self):
        return self.owner.email

class WishListItems(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)
    #wishlist = models.ForeignKey(WishList,on_delete=models.CASCADE, related_name='wishlistitems')
    item = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    wish_variants = models.ForeignKey(Variants,on_delete=models.CASCADE, related_name='wishitems')


    def __str__(self):
        return f"{self.item.name} of {self.owner.email}"

    class Meta:
        verbose_name_plural= "WishList"


class Order(models.Model):
    ORDER_STATUS = (
        ('To_Ship', 'To Ship',),
        ('Shipped', 'Shipped',),
        ('Delivered', 'Delivered',),
        ('Cancelled', 'Cancelled',),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    #order_items = models.ManyToManyField('OrderItem',blank=True, null=True)
    order_status = models.CharField(max_length=50,choices=ORDER_STATUS,default='To_Ship')
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    current_points = models.FloatField(default=0)
    total_price = models.FloatField(blank=True,null=True)
    point_spent = models.FloatField(default=0)


    def final_price(self):
        total = sum([_.price for _ in self.order_items.all()])
        total -= Decimal(self.price_of_points)
        print(total)
        return total

    @property
    def price_of_points(self):
        point_spent = self.point_spent
        print(point_spent)
        if point_spent == 0:
            return 0.0
        elif point_spent <= 10000.0 and point_spent >0:
            return 10.0
        else:
            return 75.0

    def save(self, *args, **kwargs):
        self.total_price = self.final_price()
        super(Order, self).save(*args, **kwargs)

    # def save(self, force_insert=False, **kwargs):
    #     created = force_insert or not self.pk
    #     print(self.final_price())
    #     self.total_price = self.final_price()
    #     super(Order, self).save(force_insert=force_insert, **kwargs)
    #     if created:
    #         points = Points.calculate_points(self.total_price)
    #         print(points)
    #         Points.objects.create(user=self.user, points_gained=points)


    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "Orders"
        ordering = ('-id',)

# def price(self):
#     total_item_price = self.quantity * self.item.varaints.price
#     return total_item_price



class OrderItem(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True
    #orderItem_ID = models.UUIDField(max_length=12, editable=False,default=str(uuid.uuid4()))
    orderItem_ID = models.CharField(max_length=12, editable=False, default=id_generator)
    order = models.ForeignKey(Order,on_delete=models.CASCADE, blank=True,null=True,related_name='order_items')
    item = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    order_variants = models.ForeignKey(Variants, on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(default=1)
    #price = models.IntegerField(blank=True,null=True)




    #total_item_price = models.PositiveIntegerField(blank=True,null=True,default= 0)

    ORDER_STATUS = (
        ('To_Ship', 'To Ship',),
        ('Shipped', 'Shipped',),
        ('Delivered', 'Delivered',),
        ('Cancelled', 'Cancelled',),
    )
    order_item_status = models.CharField(max_length=50,choices=ORDER_STATUS,default='To_Ship')

    @property
    def price(self):
        total_item_price = self.quantity * self.order_variants.price
        # print(total_item_price)
        return total_item_price

    # def save(self,*args,**kwargs):
    #     quantity = self.quantity
    #     price = self.get_price()
    #     self.total_item_price = quantity*price
    #     # return total_item_price
    #     super(OrderItem,self).save(*args,**kwargs)

    # def __str__(self):
    #     return f"{self.quantity} items of {self.item} of {self.order.user}"

    class Meta:
        verbose_name_plural = "Cart Items"
        ordering = ('-id',)

class BillingDetails(models.Model):
    PAYMENT_TYPE = (
        ('cash_on_delivery', 'Cash On Delivery',),
        ('credit/debit_card', 'Credit/Debit Card',),
        ('connect_ips', 'Connect IPS',),
        ('fonepay', 'Fonepay',),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='billing_details')
    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50,blank=True,null=True)
    area = models.CharField(max_length=50,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    postal = models.CharField(max_length=50,blank=True,null=True)
    payment_type = models.CharField(max_length=50,blank=True,null=True,choices=PAYMENT_TYPE,default='cash_on-delivery')
    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural= "Shipping Address"


class Points(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    points_gained = models.FloatField(blank=True,null=True)

    # @staticmethod
    # def calculate_points(amount):
    #     return 0.01 * amount if amount <= 10000 else 0.75 * amount

    # @receiver(post_save, sender=Order)
    def collect_points(sender, instance, created, **kwargs):
        total_price = (instance.total_price)
        if created == False and instance.ordered == True:
            if total_price <= 10000.0:
                abc = Decimal(0.01) * (total_price)
            else:
                abc = Decimal(0.75) * total_price
            #new_point = Points.objects.create(user=instance.user, points_gained=abc)

            try:
                    # Check if user already has points and update if so
                    points = Points.objects.get(user=instance.user)
                    old_points = Decimal(points.points_gained)
                    points.points_gained = Decimal(old_points)+abc
                    points.save(update_fields=['points_gained'])
            except Points.DoesNotExist:
                    # User does not have points yet, create points
                    Points.objects.create(user=instance.user,
                                          points_gained=abc)

    post_save.connect(collect_points, sender=Order)