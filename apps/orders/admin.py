from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.




admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(WishList)
admin.site.register(WishListItems)