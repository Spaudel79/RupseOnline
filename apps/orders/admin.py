from django.contrib import admin
from .models import *

from django.utils.html import format_html
# Register your models here.

class WishListItemsAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/orders/wishlistitems/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/wishlistitems/{}/delete/">Delete</a>', obj.id)

    #list_display = ('item', 'edit','delete')
    #list_display_links = ('name', )
    icon_name = 'color_lens'

class OrdersAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/orders/orders/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/orders/orders/{}/delete/">Delete</a>', obj.id)

    list_display = ('user', 'ordered_date', 'edit','delete')
    list_display_links = ('user', )
    icon_name = 'camera'

class OrderItemsAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/orders/orderitems/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/orders/orderitems/{}/delete/">Delete</a>', obj.id)

    # list_display = ('user', 'ordered_date', 'edit','delete')
    # list_display_links = ('user', )
    icon_name = 'add_shopping_cart'

class BillingDetailsAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/orders/billingdetails/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/orders/billingdetails/{}/delete/">Delete</a>', obj.id)

    list_display = ('email', 'first_name', 'address', 'payment_type', 'edit','delete')
    list_display_links = ('email', )
    icon_name = 'add_location'

# admin.site.register(Cart)
# admin.site.register(CartItem)
#admin.site.register(WishList)
admin.site.register(WishListItems,WishListItemsAdmin)
admin.site.register(OrderItem,OrderItemsAdmin)
admin.site.register(Order,OrdersAdmin)
admin.site.register(BillingDetails,BillingDetailsAdmin)