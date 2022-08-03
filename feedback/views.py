from django.shortcuts import redirect, render

# Create your views here.

# Home Page------------------------------------------------------
def home(request):
    return render(request, 'feedback/home.html', { })

def code(request):
    return render(request, 'feedback/code.html', { })

def emailqrcode(request):
    return render(request, 'feedback/emailqrcode.html',{})

# Handle Brand Details------------------------------------------------------
def qrcode(request):
    if request.method == 'POST':
        form = request.POST
        print(form)
        form.save()
        return redirect('/feedback/emailqrcode.html', {})
