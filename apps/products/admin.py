from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'featured', )
    list_filter = ('name', 'price', 'quantity', 'featured', )
    list_editable = ('price', 'quantity', )

    # sets up slug to be generated from product name
    # prepopulated_fields = {'slug': ('name', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    icon_name = 'assignment'

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    icon_name = 'layers'

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    icon_name = 'explore'


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = 'Rupse Online'
