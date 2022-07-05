from django.contrib import admin
from .models import Pedido, NotaPedido

# Register your models here
admin.site.register([Pedido, NotaPedido])
