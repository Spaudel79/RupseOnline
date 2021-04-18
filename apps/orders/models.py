from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product, Variants

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
    #items = models.ManyToManyField(OrderItem,blank=True, null=True,related_name="order_items")
    #start_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=50,choices=ORDER_STATUS,default='To_Ship')

    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    #total_price = models.CharField(max_length=50,blank=True,null=True)
    #billing_details = models.OneToOneField('BillingDetails',on_delete=models.CASCADE,null=True,blank=True,related_name="order")


    @property
    def total_price(self):
        # abc = sum([_.price for _ in self.order_items.all()])
        # print(abc)
        return sum([_.price for _ in self.order_items.all()])

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



    #total_item_price = models.PositiveIntegerField(blank=True,null=True,default=0)

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
        return total_item_price


    # def save(self,*args,**kwargs):
    #     quantity = self.quantity
    #     price = self.get_price()
    #     self.total_item_price = quantity*price
    #     # return total_item_price
    #     super(OrderItem,self).save(*args,**kwargs)

    def __str__(self):
        return f"{self.quantity} items of {self.item} of {self.order.user}"

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
