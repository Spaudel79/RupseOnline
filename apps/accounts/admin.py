from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import Site
from taggit.admin import Tag
from django.utils.html import format_html
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("first_name", "last_name", "email", "is_customer", "is_seller")
    list_filter = ("first_name", "last_name", "email", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal information", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active","is_customer","is_seller")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active",),
            },
        ),
    )
    list_display_links = ('email',)
    search_fields = ("first_name", "last_name", "email")
    ordering = ( "email","first_name", "last_name")
    icon_name = 'tag_faces'

class CustomerProfileAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/accounts/customer/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/accounts/customer/{}/delete/">Delete</a>', obj.id)

    list_display = ('customer', 'first_name','last_name', 'phone_num', 'edit','delete' )
    list_display_links = ('customer', )
    icon_name = 'people'

class SellerProfileAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/accounts/seller/{}/change/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/accounts/seller/{}/delete/">Delete</a>', obj.id)

    list_display = ('seller', 'first_name','last_name', 'business_name','phone_num', 'edit','delete' )
    list_display_links = ('seller', )
    icon_name = 'people_outline'


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Seller,SellerProfileAdmin)
admin.site.register(Customer,CustomerProfileAdmin)
# admin.site.register(UserType)
# admin.site.unregister(CustomUserAdmin)
admin.site.unregister(Site)
admin.site.unregister(Tag)
# admin.site.unregister(Emailaddress)
