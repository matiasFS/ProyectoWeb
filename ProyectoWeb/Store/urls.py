from django.urls import path
from Store import views

urlpatterns = [
    path('', views.store, name="Store"),

]
