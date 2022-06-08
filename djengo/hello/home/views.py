from django.shortcuts import render, HttpResponse
from datetime import datetime
from  home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    contex = {
        'variable':"this is sent"
    }

    return render(request, 'index.html', contex)
    # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contect(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contect = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contect.save()
        messages.success(request, 'Your massage has been sent!')
    return render(request, 'contect.html')
    # return HttpResponse("this is contect page")