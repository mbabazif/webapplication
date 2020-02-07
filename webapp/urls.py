from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from webapp import views
from . import views
from .views import *



urlpatterns = [
    url(r'^customer/',views.customerList, name='list'),
    
   
]