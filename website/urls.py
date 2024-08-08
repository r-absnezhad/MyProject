from django.urls import path
from website.views import *

app_name = 'website'
urlpatterns = [
    path('',index_viwe,name='index'),
    path('about',about_viwe,name='about'),
    path('contact',contact_viwe,name='contact'),
]
