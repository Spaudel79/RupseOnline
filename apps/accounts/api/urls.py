from django.urls import include, path
from .import views
from .views import *


urlpatterns = [
    path("", include("rest_auth.urls")),
    path("api/register/", include("rest_auth.registration.urls")),
    path("api/seller/register/",SellerRegisterView.as_view(), name='api-registerseller'),
    path("api/seller/login/", views.SellerLoginUserView.as_view(), name='api-seller-login' ),
    path("api/seller/profile/", views.SellerProfileView.as_view(), name='api-seller-profile' ),
    path("api/seller/profile/update", views.SellerUpdateProfileView.as_view(), name='api-seller-update' ),
    path("api/customer/register/",CustomerRegisterView.as_view(), name='api-registercustomer'),
    path("api/customer/login/", views.CustomerLoginUserView.as_view(), name='api-customer-login' ),
    path("api/login/", views.LoginUserView.as_view(), name='api-login'),
    path("api/logout/", views.Logout.as_view(), name='api-logout'),
    # path("api/register", views.RegisterUserView.as_view(), name='api-register')
]
