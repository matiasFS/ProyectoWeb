from django.urls import path
from pedidos import views

app_name = "pedidos"

urlpatterns = [
    path('', views.procesar_pedido, name="ProcesarPedidos"),

]
