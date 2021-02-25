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
    path('api/createwishlist', views.WishListAPIView.as_view(), name='api-wishlist'),
    path('api/additemwishlist/<int:pk1>/products/<int:pk2>', views.WishListItemsAPIView.as_view(), name='api-wishlistitems-add'),

    #BillingInfo-endpoints
    path('api/createaddress', views.AddressAPIView.as_view(), name='api-address-create'),

    #orders-endpoints
    path('api/addorderitem/<int:pk>', views.AddtoOrderItemView.as_view(), name='api-add-orderitem'),
    path('api/orderdetail', views.OrderDetailView.as_view(), name='api-orderdetail'),
    #path('api/addorderitem/<int:pk>', views.add_to_cart(), name='api-add-orderitem'),
    path('api/delorderitem/<int:pk>', views.DelOrderItemView.as_view(), name='api-del-orderitem'),


]
