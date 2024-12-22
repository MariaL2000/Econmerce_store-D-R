from django.contrib import admin
from .models import Carrito, CarritoProducto, Orden

class CarritoProductoInline(admin.TabularInline):
    model = CarritoProducto
    extra = 1  # Número de formularios vacíos a mostrar

class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total')
    inlines = [CarritoProductoInline]

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'carrito', 'fecha', 'total')
    list_filter = ('fecha', 'usuario')
    search_fields = ('usuario__username',)

# Registro de los modelos en el admin
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(CarritoProducto)  # Este modelo se puede registrar si deseas gestionarlo directamente