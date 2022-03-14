from distutils.command.upload import upload
from sre_parse import CATEGORIES
from tabnanny import verbose
from unicodedata import name
from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "productCategory"
        verbose_name_plural = "productCategories"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=50)
    categories = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="store", null=True, blank=True)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name
