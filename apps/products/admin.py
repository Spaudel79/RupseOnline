from django.contrib import admin
from .models import *
from django.utils.html import format_html


class VariantsAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/variants/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/variants/{}/delete/">Delete</a>', obj.id)

    list_display = ('color','size', 'price','quantity','vairant_availability', 'edit','delete')
    #list_display_links = ('name', )
    icon_name = 'assignment'

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

    list_display = ('name', 'featured', 'availability','edit', 'delete')
    icon_name = 'personal_video'


class CategoryAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/category/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/category/{}/delete/">Delete</a>', obj.id)

    list_display = ('name', 'edit','delete')
    list_display_links = ('name', )
    icon_name = 'assignment'

class BrandAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/brand/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/brand/{}/delete/">Delete</a>', obj.id)

    list_display = ('name', 'brand_category', 'edit','delete' )
    list_display_links = ('name', )
    icon_name = 'layers'

class CollectionAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/collection/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/collection/{}/delete/">Delete</a>', obj.id)

    list_display = ('name', 'edit', 'delete' )
    list_display_links = ('name', )
    icon_name = 'collections'

class ImageBucketAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/imagebucket/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/imagebucket/{}/delete/">Delete</a>', obj.id)

    list_display = ('pic', 'edit', 'delete')

    icon_name = 'camera_alt'

class ReviewAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/review/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/products/review/{}/delete/">Delete</a>', obj.id)

    list_display = ('user', 'product', 'created_at', 'edit', 'delete')
    list_display_links = ('user',)
    icon_name = 'create'

admin.site.register(Product, ProductAdmin)
admin.site.register(Variants, VariantsAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ImageBucket,ImageBucketAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.site_header = 'Rupse Online'
