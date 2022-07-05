from django.shortcuts import render
from pedidos.models import NotaPedido, Pedido
from django.contrib import messages

# Create your views here.
@login_required(login_url = "/authentication/login")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user = request.user)
    carro = Carro(request)
    notaPedido = list()
    for key, value in carro.carro.items():
        notaPedido.append(NotaPedido(
            product_id = key,
            quantity = value["quantity"],
            user = request.user,
            pedido = pedido
        ))
    NotaPedido.objects.bulk_create(notaPedido)

    send_mail(
       
    )
    messages.success(request, "El pedido se ha creado correctamente")

    return redirect("../store")