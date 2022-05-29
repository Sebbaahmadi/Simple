from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def PartyBox(request):

    return render(request,'menu/PartyBox.html')



def IceCream(request):

    return render(request,'menu/IceCream.html')



def Sweets(request):

    return render(request,'menu/Sweets.html')

def menu(request):

    return render(request,'menu/menu.html')