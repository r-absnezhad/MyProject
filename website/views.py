from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_viwe(request):
    return render(request,'website/index.html')

def about_viwe(request):
    return render(request,'website/about.html')

def contact_viwe(request):
    return render(request,'website/contact.html')


