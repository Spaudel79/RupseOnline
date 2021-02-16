from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path, re_path, include
from .import views


# from products.api.views import ProductViewSet
#
# router = DefaultRouter()
# router.register("", ProductViewSet)

urlpatterns = [
    #cart-endpoints
    path('api/cart', views.CartAPIView.as_view(), name='api-cart'),
    path('api/cart/<int:pk>', views.CartwithItemAPIView.as_view(), name='api-cart-details'),
    path('api/cartitem', views.CartItemAPIView.as_view(), name='api-cartitem'),
    path('api/cartitem/<int:pk>', views.CartItemDetailAPIView.as_view(), name='api-cartitem-detail'),
    path('api/cartitemcreate/<int:pk1>/products/<int:pk2>', views.CartItemAPIView.as_view(), name='api-cartitem-add'),
    path('api/cartitemupdate/<int:pk>', views.CartItemUpdateAPIView.as_view(), name='api-cartitem-update'),

    #wishlist-endpoints
    path('api/wishlist', views.WishListAPIView.as_view(), name='api-wishlist'),
    path('api/createwishlist/<int:pk>', views.WishListAPIView.as_view(), name='api-wishlist'),


]
