"""RupseOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from allauth.account.models import EmailAddress
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group


urlpatterns = [

    path('', admin.site.urls),
    path('', include('apps.products.api.urls')),
    path('', include('apps.accounts.api.urls')),
    path('', include('apps.orders.api.urls')),
    path('', include('apps.contacts.api.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
    # path('test/', TemplateView.as_view(template_name='base.html'), name='index'),
    # path('api', include('api.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
]

# to load static/media files in development environment
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


# admin.site.unregister(SocialToken)
# admin.site.unregister(SocialAccount)
# admin.site.unregister(SocialApp)
admin.site.unregister(EmailAddress)
admin.site.unregister(Group)