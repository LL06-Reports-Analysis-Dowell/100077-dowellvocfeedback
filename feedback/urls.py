from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("preview/", views.preview, name="preview"),
    path("help-video/", views.helpvideo, name="video"),
    path("brand-details/", views.create_Qr_Code, name="code"),
    path("email-qr-code/", views.emailqr, name="emailqr"),
    path("show-qr-code/", views.showqr, name="showqr"),
    path("recommend-friend/", views.recommend, name="recommend"),
    path("privacy-policy/", views.policy, name="policy"),
    path("brandurl/", views.feedback, name="feedback"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
