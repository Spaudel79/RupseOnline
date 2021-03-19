from django.contrib import admin
from .models import AboutUs, Contact,Choose,ContactInfo
from django.utils.html import format_html

# Register your models here.

class AboutUsAdmin(admin.ModelAdmin):

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/contacts/aboutus/{}/delete/">Delete</a>', obj.id)

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/contacts/aboutus/{}/edit/">Change</a>', obj.id)

    # list_display = ('full_name', 'email', 'phone', 'delete')

    #list_display = []
    icon_name = 'person_pin'

class ContactAdmin(admin.ModelAdmin):
    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/contacts/contact/{}/delete/">Delete</a>', obj.id)

    list_display = ('full_name', 'email', 'phone', 'delete')
    list_display_links = ('email', )
    icon_name = 'folder_open'

class ChooseAdmin(admin.ModelAdmin):
    #list_display = []
    icon_name = 'account_box'

class ContactInfoAdmin(admin.ModelAdmin):

    def edit(self, obj):
        return format_html('<a class="btn-btn" href="/admin/contacts/contactinfo/{}/edit/">Change</a>', obj.id)

    def delete(self, obj):
        return format_html('<a class="btn-btn" href="/admin/contacts/contactinfo/{}/delete/">Delete</a>', obj.id)

    list_display = ('web_url','edit','delete')
    icon_name = 'local_florist'

admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Choose,ChooseAdmin)
admin.site.register(ContactInfo,ContactInfoAdmin)
