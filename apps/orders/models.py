from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product,Variants
# import settings

# Create your models here.

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
    wish_variants = models.OneToOneField(Variants,on_delete=models.CASCADE, related_name='wishitems')


    def __str__(self):
        return f"{self.item.name} of {self.owner.email}"

    class Meta:
        verbose_name_plural= "WishList"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    #items = models.ManyToManyField(OrderItem,blank=True, null=True,related_name="order_items")
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    #billing_details = models.OneToOneField('BillingDetails',on_delete=models.CASCADE,null=True,blank=True,related_name="order")

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural= "Orders"

class OrderItem(models.Model):
    #user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE, blank=True,null=True,related_name='order_items')
    item = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} items of {self.item} of {self.order.user}"

    class Meta:
        verbose_name_plural= "Cart Items"


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
    country = models.CharField(max_length=50,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    postal = models.CharField(max_length=50,blank=True,null=True)
    payment_type = models.CharField(max_length=50,blank=True,null=True,choices=PAYMENT_TYPE,default='cash_on-delivery')
    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural= "Shipping Address"
