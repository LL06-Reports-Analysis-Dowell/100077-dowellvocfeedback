from django.shortcuts import redirect, render

# Create your views here.

# Home Page------------------------------------------------------
def home(request):
    return render(request, 'feedback/home.html', { })

# Brand Details------------------------------------------------------
def code(request):
    return render(request, 'feedback/code.html', { })

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

# 
def confirm(request):
    return render(request, 'feedback/emailconfirmation.html',{})


# Handle Brand Details------------------------------------------------------
def createQrCode(request):
    if request.method == 'POST':
        form = request.POST
        print(form)
        form.save()
        return redirect('feedback/showqrcode.html', {})
    else:
        return render(request, 'feedback/emailqrcode.html',{})

def error_404_view(request, exception):
    return render(request, 'feedback/404.html', {}, status=404)