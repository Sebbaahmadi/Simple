from django.shortcuts import render
from . models import Contact
from django.http import HttpResponse 

# Create your views here.
def home(request):
    return render(request,'page/home.html')

def about(request):
    return render(request,'page/about.html')

def contact(request):

    if request.method=="POST":
        contact=Contact()
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        Message=request.POST.get('Message')
        contact.Name=Name
        contact.Email=Email
        contact.Message=Message
        contact.save()
        return HttpResponse("<h1> THANK YOU FOR CONTACT US <h1> ")
    return render(request,'page/contact.html')




     