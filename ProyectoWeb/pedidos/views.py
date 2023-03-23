from django.shortcuts import render
from flask import redirect
from pedidos.models import NotaPedido, Pedido
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
# Create your views here.

@login_required(login_url = "/authentication/login")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user = request.user)
    cart = Cart(request)
    notaPedido = list()
    for key, value in cart.cart.items():
        notaPedido.append(NotaPedido(
            product_id = key,
            cantidad = value["quantity"],
            user = request.user,
            pedido = pedido
        ))
    NotaPedido.objects.bulk_create(notaPedido)

    enviar_mail(
       pedido = pedido,
       notaPedido = notaPedido,
       nombreusuario = request.user.username,
       emailusuario = request.user.email
    )
    messages.success(request, "El pedido se ha creado correctamente")

    return redirect("../store")

def enviar_mail(**kwargs):
    asunto= "Gracias por su pedido"
    mensaje= render_to_string("emails/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "notaPedido": kwargs.get("notaPedido"),
        "nombreusuario": kwargs.get("nombreusuario")
        
    })
    
    mensaje_texto= strip_tags(mensaje)
    from_email=""
    to=""
    
    send_mail(asunto, mensaje_texto, from_email,[to],html_message=mensaje)