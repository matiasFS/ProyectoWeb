from django.shortcuts import render
from Services.models import Services

# Create your views here.
def services(request):
    services = Services.objects.all()
    return render(request, "Services/services.html", {"services":services})