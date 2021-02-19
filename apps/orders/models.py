from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product
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
    wishlist = models.ForeignKey(WishList,on_delete=models.CASCADE, related_name='wishlistitems')
    item = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)


    def __str__(self):
        return self.item.name

class OrderItem(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True, null=True)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    items = models.ManyToManyField(OrderItem,blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
