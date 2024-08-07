from django.urls import path
from website.views import *

urlpatterns = [
    path('',index_viwe,name='index'),
    path('about',about_viwe,name='about'),
    path('contact',contact_viwe,name='contact'),
]
