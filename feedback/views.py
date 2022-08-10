from django.shortcuts import redirect, render
from .models import Brand
from feedback.qrcode_gen import qrgen
from django.conf import settings
from django.core.mail import send_mail




# Create your views here.
def error_404_view(request, exception):
    return render(request, 'feedback/404.html', {}, status=404)

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

        # print(context)

        return redirect('/recommend-friend/', context)

    return render(request, 'feedback/emailqrcode.html',{})


# Handle Brand Details------------------------------------------------------
def create_Qr_Code(request):

    context = {}

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

        # create QR from brand data.
        qrgen(brand_logo, link, brand_product_name, brand_name, outimg)

        # Save Brand Data   
        brand = Brand(brand_logo=brand_logo, brand_name=brand_name, brand_product_name=brand_product_name, brand_qr_code_picture=outimg, brand_qr_code_url=brand_qr_code_url)
        brand.save()

        context["brand_qr_code_url"] = brand_qr_code_url


        return redirect('/show-qr-code/' , context)
    return render(request, 'feedback/code.html')