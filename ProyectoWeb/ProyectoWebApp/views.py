from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home")

def serivces(request):
    return HttpResponse("Services")

def store(request):
    return HttpResponse("Store")

def blog(request):
    return HttpResponse("Blog")

def contact(request):
    return HttpResponse("Contact")