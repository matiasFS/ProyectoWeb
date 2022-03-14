from django.shortcuts import render, redirect
from .cart import Cart
from Store.models import Products

# Create your views here.


def addProduct(request, product_id):
    cart = Cart(request)
    product = Products.objects.get(id=product_id)
    cart.add_product(product)

    return redirect("Store")


def deleteProduct(request, product_id):
    cart = Cart(request)
    product = Products.objects.get(id=product_id)
    cart.delete_product(product)

    return redirect("Store")


def subtractProduct(request, product_id):
    cart = Cart(request)
    product = Products.objects.get(id=product_id)
    cart.subtract_product(product)

    return redirect("Store")


def cleanCart(request, product_id):
    cart = Cart(request)
    cart.clean_cart()
    return redirect("Store")
