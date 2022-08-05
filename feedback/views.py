from django.shortcuts import redirect, render

from feedback.models import Brand

# Create your views here.

# Home Page------------------------------------------------------
def home(request):
    return render(request, 'feedback/home.html', { })


# Show QR Code ------------------------------------------------------
def showqr(request):
    return render(request, 'feedback/showqrcode.html',{})

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
def createQrCode(request):
    # print(request.POST)
    if request.method == 'POST':
        brand_logo = request.FILES['brand_picture']
        brand_name = request.POST['brand_name']
        brand_product_name = request.POST['brand_product_name']
        new_brand = Brand(brand_logo=brand_logo, brand_name=brand_name, brand_product_name=brand_product_name)
        new_brand.save()
        return redirect('/show-qr-code/')
    else:
        return render(request, 'feedback/code.html',{})

def error_404_view(request, exception):
    return render(request, 'feedback/404.html', {}, status=404)