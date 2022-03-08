from django.contrib import admin
from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('services', views.serivces, name="Services"),
    path('store', views.store, name="Store"),
    path('blog', views.blog, name="Blog"),
    path('contact', views.contact, name="Contact"),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)