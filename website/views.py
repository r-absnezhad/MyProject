from django.shortcuts import render
from django.http import HttpResponse
from website.forms import ContactForm
from django.contrib import messages

# Create your views here.

def index_viwe(request):
    return render(request,'website/index.html')

def about_viwe(request):
    return render(request,'website/about.html')

def contact_viwe(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'WELL DONE! SUBMITTED SUCCESSFULLY! ')
        else:
            messages.add_message(request,messages.ERROR, 'OOPS! NOT SUBMITTED SUCCESSFULLY! ')

    form = ContactForm()       
    return render(request,'website/contact.html',{'form':form})

