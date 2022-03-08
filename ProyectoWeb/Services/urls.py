from django.urls import path
from Services import views

urlpatterns = [
    path('', views.services, name="Services"),


]
