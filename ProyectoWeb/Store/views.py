from django.shortcuts import render

from Store.models import Products

# Create your views here.
def store(request):
    products = Products.objects.all()
    return render(request, "store/store.html", {"products": products})