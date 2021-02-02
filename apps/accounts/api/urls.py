from django.urls import include, path
from .import views
from .views import *


urlpatterns = [
    path("", include("rest_auth.urls")),
    path("api/register/", include("rest_auth.registration.urls")),
    path("api/login/",views.LoginUserView.as_view(), name='api-login' ),
    path("api/vendorlogin/",views.VendorLoginUserView.as_view(), name='api-vendorlogin'),
    path("api/logout/",views.Logout.as_view(), name='api-logout' ),
    # path("api/register", views.RegisterUserView.as_view(), name='api-register')
]
