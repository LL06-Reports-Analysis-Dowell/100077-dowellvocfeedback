import os
import qrcode
from django.shortcuts import redirect, render
from feedback.models import Brand
from feedback.qrcode_gen import qrgen



# Create your views here.


# Home Page------------------------------------------------------
def home(request):
    return render(request, 'feedback/home.html', { })


# Show QR Code ------------------------------------------------------
def showqr(request):
    brand = Brand()
    print(brand)

    return render(request, 'feedback/showqrcode.html',{ 'brand': brand })

# Preview Page------------------------------------------------------
def preview(request):
    return render(request, 'feedback/preview.html',{})

# Help Video------------------------------------------------------
def helpvideo(request):
    return render(request, 'feedback/help-video.html',{})

# Privacy Policy------------------------------------------------------
def policy(request):
    return render(request, 'feedback/policy.html',{})

# Recommend Friend------------------------------------------------------
def recommend(request):
    return render(request, 'feedback/recommendfriend.html',{})

# Confirm email------------------------------------------------------
def confirm(request):
    return render(request, 'feedback/emailconfirmation.html',{})

# Email Qr Code------------------------------------------------------
def emailqr(request):
    return render(request, 'feedback/emailqrcode.html',{})


# Handle Brand Details------------------------------------------------------
def create_Qr_Code(request):

    # Application Link
    link = 'http://127.0.0.1:8000/'

    # Path to save qr code
    outimg = 'media/qrcodes/qr.png'
    
    # Get Brand Data
    if request.method == 'POST':
        brand_logo = request.FILES['brand_picture']
        brand_name = request.POST['brand_name']
        brand_product_name = request.POST['brand_product_name']
        brand_qr_code_url =  f'{link}?brand={brand_name}&product={brand_product_name}&logo={outimg}'

        print(brand_qr_code_url)

        # create QR from brand data.
        qrgen(brand_logo, link, brand_product_name, brand_name, outimg)

        # Save Brand Data   
        brand = Brand(brand_logo=brand_logo, brand_name=brand_name, brand_product_name=brand_product_name, brand_qr_code_picture=outimg, brand_qr_code_url=brand_qr_code_url)
        brand.save()

        return redirect('/show-qr-code/' ,{'brand_qr_code_url': brand_qr_code_url})
    else:
        return render(request, 'feedback/code.html')


def error_404_view(request, exception):
    return render(request, 'feedback/404.html', {}, status=404)