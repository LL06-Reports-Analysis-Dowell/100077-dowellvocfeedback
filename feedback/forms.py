from django import forms
from .models import Brand


class BrandInfoForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name', 'brand_product_name', 'brand_picture', 'brand_qr_code_url', 'brand_qr_code_picture', 'brand_user_name', 'brand_user_email']