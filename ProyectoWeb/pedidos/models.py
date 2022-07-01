from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField
# Create your models here.
User = get_user_model()

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.notapedido_set.aggregate(
            total = Sum(F("precio")*F("cantidad"), output_field = FloatField())
        )["total"]

    class Meta:
        db_table = 'pedido'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']

class NotaPedido(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    cantidad = models.IntegerField(default = 1)
    created_at = models.DateTimeField(auto)

    def __str__(self):
        return f'{self.cantidad} + unidades de {self.product_id.nombre}'

    class Meta:
        db_table = 'notapedidos'
        verbose_name = 'Nota pedido'
        verbose_name_plural = 'Nota Pedidos'
        ordering = ['id']
