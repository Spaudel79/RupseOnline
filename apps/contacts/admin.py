from django.contrib import admin
from .models import AboutUs, Contact
from django.utils.html import format_html

# Register your models here.

class AboutUsAdmin(admin.ModelAdmin):
    #list_display = []
    icon_name = 'person_pin'

class ContactAdmin(admin.ModelAdmin):
    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/contacts/contact/{}/delete/">Delete</a>', obj.id)

    list_display = ('full_name', 'email', 'phone', 'delete')
    list_display_links = ('email', )
    icon_name = 'folder_open'



admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(Contact,ContactAdmin)
