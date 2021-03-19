from django.urls import path
from .import views


urlpatterns = [
    path('api/aboutus',views.AboutUsAPIView.as_view(),name='api-aboutus'),
    path('api/contact',views.ContactAPIView.as_view(),name='api-contact'),
    path('api/rupseinfo',views.RupseAPIView.as_view(),name='api-rupse'),
]