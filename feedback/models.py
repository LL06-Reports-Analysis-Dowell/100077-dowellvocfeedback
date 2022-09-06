from django.db import models

# Create your models here.

# Brand------------------------------------------------------
class Brand(models.Model):
    brand_name = models.CharField(max_length=250)
    brand_product_name = models.CharField(max_length=250)
    brand_logo = models.ImageField(upload_to='brandlogos/', null=True, blank=True)
    brand_qr_code_url = models.CharField(max_length=600, null=True, blank=True)
    brand_qr_code_picture = models.ImageField(upload_to='brandqrcodes/', null=True, blank=True)
    brand_user_name = models.CharField(max_length=250, null=True, blank=True)

# User-----------------------------------------------------------
class User(models.Model):
    user_name = models.CharField(max_length=300)
    user_password = models.CharField(max_length=300)
    user_info_qrcode = models.ImageField(upload_to='userqrcodes/', null=False, blank=False)
