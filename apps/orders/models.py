from django.db import models
from django.contrib.auth import get_user_model
from apps.products.models import Product

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
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item.name