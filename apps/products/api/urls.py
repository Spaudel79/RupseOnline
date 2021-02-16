from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path, re_path, include
from .import views


# from products.api.views import ProductViewSet
#
# router = DefaultRouter()
# router.register("", ProductViewSet)

urlpatterns = [
    path('api/category', views.CategoryAPIView.as_view(), name='api-category'),
    path('api/brand', views.BrandAPIView.as_view(), name='api-brand'),
    path('api/collection', views.CollectionAPIView.as_view(), name='api-collection'),
    path('api/products', views.ProductAPIView.as_view(), name='api-products'),
    path('api/products/<int:pk>', views.ProductDetailAPIView.as_view(), name='api-products-detail'),
    # path('api/addcategories', views.CategoryAddAPIView.as_view(), name='api-addcategory'),
    # path('api/addbrand', views.BrandAddAPIView.as_view(), name='api-addbrand'),
    # path('api/addcollection', views.CollectionyAddAPIView.as_view(), name='api-addcollection'),
    path('api/addproducts', views.ProductAddAPIView.as_view(), name='api-addproducts'),

]
