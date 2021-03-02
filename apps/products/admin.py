from django.contrib import admin
from .models import *
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    # list_display = ('name', 'price', 'quantity', 'featured', )
    # list_filter = ('name', 'price', 'quantity', 'featured', )
    # list_editable = ('price', 'quantity', )
    #
    # # sets up slug to be generated from product name
    # # prepopulated_fields = {'slug': ('name', )}

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/product/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/product/{}/delete/">Delete</a>', obj.id)

    list_display = ('name', 'featured', 'availability', 'price','edit', 'delete')
    icon_name = 'explore'


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
admin.site.register(ImageBucket)
admin.site.site_header = 'Rupse Online'
