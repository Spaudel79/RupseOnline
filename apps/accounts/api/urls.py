from django.urls import include, path
from .import views
from .views import *


urlpatterns = [
    path("", include("rest_auth.urls")),
    path("api/register/", include("rest_auth.registration.urls")),
    path("api/seller/register/",SellerRegisterView.as_view(), name='api-registerseller'),
    path("api/seller/login/", views.SellerLoginUserView.as_view(), name='api-seller-login' ),
    path("api/seller/profile/", views.SellerProfileView.as_view(), name='api-seller-profile' ),
    path("api/seller/profile/update/<int:pk>", views.SellerUpdateProfileView.as_view(), name='api-seller-update' ),
    path('api/seller/token', views.SellerTokenView.as_view(), name='api-seller-token'),

    path("api/customer/register/",CustomerRegisterView.as_view(), name='api-registercustomer'),
    path("api/customer/login/", views.CustomerLoginUserView.as_view(), name='api-customer-login' ),
    path("api/customer/profile/", views.CustomerProfileView.as_view(), name='api-customer-profile' ),
    path("api/customer/profile/update/<int:pk>", views.CustomerUpdateView.as_view(), name='api-customer-profile-update' ),

    path('api/customer/token', views.CustomerTokenView.as_view(), name='api-customer-token'),
    path("api/login/", views.LoginUserView.as_view(), name='api-login'),
    path("api/logout/", views.Logout.as_view(), name='api-logout'),
    path("api/users/online", views.OnlineUsers.as_view(), name='api-online'),
    # path("api/register", views.RegisterUserView.as_view(), name='api-register')
]
