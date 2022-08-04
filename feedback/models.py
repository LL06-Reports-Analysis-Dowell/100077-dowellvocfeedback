from django.db import models

# Create your models here.

# Brand------------------------------------------------------
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_product_name = models.CharField(max_length=100)
    brand_picture = models.FileField(upload_to='uploads/%Y/%m/%d/')
    brand_qr_code_url = models.CharField(max_length=500)
    brand_qr_code_picture = models.FileField(upload_to='uploads/%Y/%m/%d/')
    brand_user_name = models.CharField(max_length=100)
    brand_user_email = models.EmailField()

    def __str__(self):
        return self.brand_name
