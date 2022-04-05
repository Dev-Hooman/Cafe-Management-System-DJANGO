from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('aboutus', views.about, name="about"),
    path('contactus', views.contactus, name="contact"),
    
]
