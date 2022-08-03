from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('code/', views.code, name='code'),
    path('emailqrcode/', views.emailqrcode, name='qrcode'),
    
]