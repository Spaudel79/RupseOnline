from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import Site
from taggit.admin import Tag

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("first_name", "last_name", "email", "is_staff", "is_active")
    list_filter = ("first_name", "last_name", "email", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal information", {"fields": ("first_name", "last_name")}),
        ("Permissions", {"fields": ("is_staff", "is_active","is_seller", "is_customer")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("first_name", "last_name", "email")
    ordering = ("first_name", "last_name", "email")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Seller)
# admin.site.register(UserType)
# admin.site.unregister(CustomUserAdmin)
admin.site.unregister(Site)
admin.site.unregister(Tag)
# admin.site.unregister(Emailaddresses)
