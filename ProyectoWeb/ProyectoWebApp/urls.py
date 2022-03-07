from django.contrib import admin
from django.urls import path
from ProyectoWebApp import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('services', views.serivces, name="Services"),
    path('store', views.store, name="Store"),
    path('blogg', views.blog, name="Blog"),
    path('contact', views.contact, name="Contact"),

]