from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoModelAdmin(admin.ModelAdmin):
    list_display= ('id', 'nombre', 'precio', 'precio_descuento','descripcion', 'imagen', 'categoria', 'cantidad_stock')
# Register your models here.
