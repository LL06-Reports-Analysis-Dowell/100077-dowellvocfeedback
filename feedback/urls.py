from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('preview/', views.preview, name='preview'),
    path('help-video/', views.helpvideo, name="video"),
    path('brand-details/', views.code, name='code'),
    path('show-qr-code/', views.showqr, name='showqr'),
    path('email-qr-code/', views.createQrCode, name='qrcode'),
    path('email-confirmation/', views.confirm, name='confirmmail'),
    path('recommend-friend/', views.recommend, name='recommend'),
    path('privacy-policy/', views.policy, name='policy'), 
]