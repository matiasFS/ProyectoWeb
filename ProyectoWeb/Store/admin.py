from django.contrib import admin
from .models import ProductCategory, Products

# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Products, ProductsAdmin)