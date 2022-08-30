from django.shortcuts import render
from django.conf import settings
from django.utils.html import strip_tags
from django.core.mail import send_mail
from PIL import Image
from cryptography.fernet import Fernet
from feedback.qrcode_gen import qrgen
from .models import Brand


# Encode Function
def encode(key,text):
    cipher_suite = Fernet(key.encode())
    encoded_text = cipher_suite.encrypt(text.encode())
    return encoded_text

def decode(key,decodetext):
    cipher_suite = Fernet(key.encode())
    decoded_text = cipher_suite.decrypt(decodetext.encode())
    return decoded_text.decode()
# Encryption Key------------------------------------------------------
key="l6h8C92XGJmQ_aXpPN7_VUMzA8LS8Bg50A83KNcrVhQ="

# Base URL------------------------------------------------------
base_url = 'http://127.0.0.1:8000/'

# Create your views here.
def error_404_view(request, exception):

    return render(request, 'feedback/404.html', {}, status=404)

# Home Page------------------------------------------------------
def home(request):
    return render(request, 'feedback/home.html', { })


# Preview Page------------------------------------------------------
def preview(request):
    return render(request, 'feedback/preview.html')


# Help Video------------------------------------------------------
def helpvideo(request):
    return render(request, 'feedback/help-video.html',{})



# Handle Brand Details------------------------------------------------------
def create_Qr_Code(request):

    context = {}
   

    # Get Brand Data
    if request.method == 'POST':
        # Get from request ans encode it
        brand_name_raw = request.POST['brand_name']
        brand_name  = encode(key,brand_name_raw)
        brand_product_name_raw = request.POST['brand_product_name']
        brand_product_name = encode(key,brand_product_name_raw)

        # Get Brand Image, Encode & Format name
        brand_logo_raw = request.FILES['brand_picture']
        brand_logo_formatted = brand_logo_raw.name.replace(" ","")
        brand_logo = encode(key,brand_logo_formatted)

        # Application Links
        brand_qr_code_url =  f"{base_url}brandurl/?brand={brand_name}&product={brand_product_name}&logo={brand_logo.decode()}"
       
        

        # create QR from brand data.
        qrgen(brand_logo_raw, f"{base_url}brandurl", brand_name.decode(), brand_product_name.decode(), f"media/qrcodes/{brand_logo_formatted}",brand_logo.decode())

        # Save Brand Data   
        brand = Brand(brand_name=brand_name, brand_product_name=brand_product_name, brand_logo=brand_logo_raw,  brand_qr_code_picture=f'media/qrcodes/{brand_logo_formatted}', brand_qr_code_url=brand_qr_code_url)
        brand.save()

        # save the diff thumbnail for the brand logo
        with Image.open(f"media/qrcodes/{brand_logo_formatted}") as image:
            image.thumbnail((128,128))
            image.save(f"media/qrcodes/thumbnails/{brand_logo_formatted}","JPEG")
        with Image.open(f"media/brandlogos/{brand_logo_raw.name.replace(' ','_')}") as image:
            image.thumbnail((256,256))
            image.save(f"media/brandlogos/thumbnails/{brand_logo_formatted}",quality=100)

        

        brand_qr_code_url = f"{base_url}brandurl?brand={brand_name.decode()}&product={brand_product_name.decode()}&logo={brand_logo.decode()}"
        
        context["brand_qr_code_url"] = brand_qr_code_url
        context["brand_qr_code_picture"] = brand_logo_formatted
        context["brand"] = brand_name_raw
        context["product"] = brand_product_name_raw
        context['base_url'] = base_url

        # return to Show QR page
        return render(request, 'feedback/showqrcode.html' , context)
    return render(request, 'feedback/code.html')

# Privacy Policy------------------------------------------------------
def policy(request):
    return render(request, 'feedback/policy.html',{})


# Pass Brand Data to Template------------------------------------------------------
def showqr(request):
    if request.method == 'POST':
        brand_qr_code_picture = request.POST['brand_qr_code_picture']
        brand_qr_code_url = request.POST['brand_qr_code_url']
        base_url = request.POST['base_url']

        context = {}
        context["brand_qr_code_picture"] = brand_qr_code_picture
        context['brand_qr_code_url'] = brand_qr_code_url
        context['base_url'] = base_url
        return render(request, 'feedback/emailqrcode.html', context)



# Send Email------------------------------------------------------
def emailqr(request):

    context = {}

    # Find Email Address
    if request.method == 'POST':
        brand_user_name = request.POST['brand_user_name']
        email = request.POST['user_email']
        brand_qr_code_picture = request.POST['brand_qr_code_picture']
        brand_qr_code_url = request.POST['brand_qr_code_url']

        # URL to QR Code Image
        brand_qr_code_picture_url = f"{base_url}media/qrcodes/{brand_qr_code_picture}"

        # Pass data to next tempate
        context["email"] = email

        # Mail Content
        subject = 'Embed your Feedback Code to your website.'
        htmlgen =  f"<div style='padding: 50px'>Dear {brand_user_name}, <br> QR code link  is <strong><a href='{brand_qr_code_picture_url}'>{brand_qr_code_picture_url}</a></strong> <br/> <h2><br> Embed this code to your website or copy and paste below your website</h2><br> <div style='text-align: center;'><img src='http://127.0.0.1:8000/media/qrcodes/{brand_qr_code_picture}' alt='qr_code'  style='height: 200px; width: 200px;' /></div><br><code>&lt;iframe width='300' height='500' style='background-color:white' src='{brand_qr_code_url}' style='-webkit-transform:scale(0.7);-moz-transform-scale(0.7);' FRAMEBORDER='no' BORDER='0' SCROLLING='no'&gt;&lt;/iframe&gt;</code><br><br><br> Best regards, <br> <strong>Voice of Customer Feedback Team</strong></div>"
        plain_message = strip_tags(htmlgen)
        from_email = settings.EMAIL_HOST_USER
        
        # Send Email
        send_mail(subject, plain_message, from_email, [email], fail_silently=False, html_message=htmlgen)


        return render(request, 'feedback/recommendfriend.html', context)


# Recommend Friend------------------------------------------------------
def recommend(request):
    if request.method == 'POST':
        email = request.POST['email']
        friend_name = request.POST['brand_user_name']
        friend_email = request.POST['friend_email']

        # Mail Content
        subject = 'Voice of Customer Feedback'
        message = 'Your QR Code is attached to this email.'
        htmlgen = '<h1>Dear { friend_name },</h1> <br> <p>Give your user ability to review your brand and manage the feedback.,Embed the QR Code in your website or app. </p> <br/>'
        from_email = settings.EMAIL_HOST_USER

        # Send Email
        send_mail(subject, message, from_email, [friend_email], fail_silently=False, html_message=htmlgen)

        return render(request, 'feedback/thankyou.html')

    return render(request, 'feedback/recommendfriend.html',{})

def feedback(request):
    context = {}
    # Brand Data & Rating
    if request.method == 'POST':
        rating = request.POST['rating']
        brand_name_encoded = request.POST['brand_name']
        brand_product_name = request.POST['brand_product_name']

        context['success'] = 'Thank you for your feedback.'
        return render(request, 'feedback/thankyou.html', context)

    #  From the Request URL.
    brand_name_encoded = request.GET.get('brand', None)
    brand_name = decode(key, brand_name_encoded)
    brand_product_name_encoded = request.GET.get('product', None)
    brand_product_name = decode(key, brand_product_name_encoded)
    brand_logo_encoded = request.GET.get('logo', None)
    brand_logo = decode(key, brand_logo_encoded)

    # Pass Brand Data to Template------------------------------------------------------
    context['brand_name'] = brand_name
    context['brand_product_name'] = brand_product_name
    context['brand_logo'] = brand_logo

    return render(request, 'feedback/feedback.html', context)