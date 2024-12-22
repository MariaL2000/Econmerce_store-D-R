from rest_framework import serializers
from .models import Carrito, CarritoProducto, Orden

class CarritoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarritoProducto
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    productos = CarritoProductoSerializer(many=True, read_only=True, source='carritoproducto_set')

    class Meta:
        model = Carrito
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'