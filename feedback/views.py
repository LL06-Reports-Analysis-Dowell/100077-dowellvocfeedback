from django.shortcuts import redirect, render

# Create your views here.

# Home Page------------------------------------------------------
def home(request):
    return render(request, 'feedback/home.html', { })

def code(request):
    return render(request, 'feedback/code.html', { })

# Handle Brand Details------------------------------------------------------
def submit_brand_details(request):
    if request.method == 'POST':
        form = request.POST
        print(form)
        form.save()
        return redirect('/feedback/emailqrcode/')
