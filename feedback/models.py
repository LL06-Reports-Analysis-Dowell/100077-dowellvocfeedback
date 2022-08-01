from django.db import models

# Create your models here.

# Brand------------------------------------------------------
class Brand(models.Model):
    brand_picture = models.ImageField(upload_to='brand_pictures/')
    brand_name = models.CharField(max_length=100)
    brand_product_name = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name
