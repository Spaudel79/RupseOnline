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

    #Merchant-endpoints
    path('api/addproducts', views.ProductAddAPIView.as_view(), name='api-addproducts'),
    path('api/seller/products/<int:pk>', views.SellerProductsAPIView.as_view(), name='api-seller-products'),
    path('api/delproducts/<int:pk>', views.ProductDeleteView.as_view(), name='api-delproducts'),
    path('api/updateproducts/<int:pk>', views.ProductUpdateView.as_view(), name = 'api-updateproducts'),

    #search-filter-endpoints
    path('api/productsearch',views.PrdouctSearchAPIView.as_view(),name='api-productsearch'),

    #review-products-endpoints
    path('api/getcreatedellreview/<int:pk>', views.GetCreateReviewAPIView.as_view(),name='api-addreview'),
    path('api/getreview', views.GetReviewAPIView.as_view(),name='api-getreview'),


]
