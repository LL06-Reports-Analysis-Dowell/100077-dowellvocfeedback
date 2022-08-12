from django.shortcuts import redirect, render
from .models import Brand
from feedback.qrcode_gen import qrgen
from django.conf import settings
from django.core.mail import send_mail
from PIL import Image


# Create your views here.
def error_404_view(request, exception):

    return render(request, 'feedback/404.html', {}, status=404)

# Home Page------------------------------------------------------
def home(request):
    return render(request, 'feedback/home.html', { })


# Show QR Code ------------------------------------------------------
def showqr(request):
    
    return render(request, 'feedback/showqrcode.html')

# Preview Page------------------------------------------------------
def preview(request):
    return render(request, 'feedback/preview.html')

# Help Video------------------------------------------------------
def helpvideo(request):
    return render(request, 'feedback/help-video.html',{})

# Privacy Policy------------------------------------------------------
def policy(request):
    return render(request, 'feedback/policy.html',{})

# Recommend Friend------------------------------------------------------
def recommend(request):
    return render(request, 'feedback/recommendfriend.html',{})


# Email Qr Code------------------------------------------------------
def emailqr(request):

    context = {}

    # Find Email Address
    if request.method == 'POST':
        brand_user_name = request.POST['brand_user_name']
        email = request.POST['user_email']

        # Brand Data
        

        # Mail Content
        subject = 'Voice of Customer Feedback'
        message = 'Your QR Code is attached to this email.'
        htmlgen = '<h1>Dear user,</h1> <br> <p>Give your user ability to review your brand and manage the feedback.,Embed the QR Code in your website or app. </p> <br/> <strong>QR Code Link<a href="http://127.0.0.1:8000/media/qrcodes/qr.png">http://127.0.0.1:8000/media/qrcodes/qr.png</a></strong> <p> Thanks, </p> <p> Voice of Customer-Feedback</p>'
        from_email = settings.EMAIL_HOST_USER
        

        # Send Email
        send_mail(subject, message, from_email, [email], fail_silently=False, html_message=htmlgen)

        context["email"] = email
        context["brand_user_name"] = brand_user_name

        return render(request, 'feedback/recommendfriend.html', context)

    return render(request, 'feedback/emailqrcode.html',{})


# Handle Brand Details------------------------------------------------------
def create_Qr_Code(request):

    context = {}

    # Get Brand Data
    if request.method == 'POST':
        brand_logo = request.FILES['brand_picture']
        brand_name = request.POST['brand_name']
        brand_product_name = request.POST['brand_product_name']

        # Application Link
        brand_qr_code_url =  f"http://127.0.0.1:8000/brandurl/?brand={brand_name}&product={brand_product_name}&logo={brand_logo}"

        # Formart Brand Logo
        brand_logo1 = brand_logo.name.replace(" ","")

        # create QR from brand data.
        qrgen(brand_logo, brand_qr_code_url, brand_name, brand_product_name, f"media/qrcodes/{brand_logo1}",brand_logo)

        # Save Brand Data   
        brand = Brand(brand_name=brand_name, brand_product_name=brand_product_name, brand_logo=brand_logo,  brand_qr_code_picture=f'media/qrcodes/{brand_logo1}', brand_qr_code_url=brand_qr_code_url)
        brand.save()

        # save the diff thumbnail for the brand logo
        with Image.open(f"media/qrcodes/{brand_logo1}") as image:
            image.thumbnail((128,128))
            image.save(f"media/qrcodes/thumbnails/{brand_logo1}","JPEG")
        with Image.open(f"media/brandlogos/{brand_logo.name.replace(' ','_')}") as image:
            image.thumbnail((256,256))
            image.save(f"media/brandlogos/thumbnails/{brand_logo1}",quality=100)

        # return to Show QR page
        context["brand_qr_code_url"] = brand_qr_code_url
        context["brand_qr_code_picture"] = brand_logo1
        context["brand"] = brand_name
        context["product"] = brand_product_name

        return render(request, 'feedback/showqrcode.html' , context)
    return render(request, 'feedback/code.html')