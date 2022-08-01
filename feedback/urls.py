from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('code/', views.code, name='code'),
    path('submit_brand_details/', views.submit_brand_details, name='submit_brand_details'),
    
]