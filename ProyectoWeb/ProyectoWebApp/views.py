from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "ProyectoWebApp/home.html")

def serivces(request):
    return render(request, "ProyectoWebApp/services.html")

def store(request):
    return render(request, "ProyectoWebApp/store.html")

def blog(request):
    return render(request, "ProyectoWebApp/blog.html")

def contact(request):
    return render(request, "ProyectoWebApp/contact.html")