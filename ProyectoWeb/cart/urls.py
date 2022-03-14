from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("add/<int:product_id>", views.addProduct, name="add"),
    path("delete/<int:product_id>", views.deleteProduct, name="delete"),
    path("subtract/<int:product_id>", views.subtractProduct, name="subtract"),
    path("clean/", views.cleanCart, name="clean"),

]
