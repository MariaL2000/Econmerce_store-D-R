from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Carrito, CarritoProducto, Orden
from .serializers import CarritoSerializer, CarritoProductoSerializer, OrdenSerializer

class CarritoList(APIView):
    def get(self, request):
        carritos = Carrito.objects.all()
        serializer = CarritoSerializer(carritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarritoDetail(APIView):
    def get(self, request, pk):
        carrito = Carrito.objects.get(pk=pk)
        serializer = CarritoSerializer(carrito)
        return Response(serializer.data)

    def put(self, request, pk):
        carrito = Carrito.objects.get(pk=pk)
        serializer = CarritoSerializer(carrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        carrito = Carrito.objects.get(pk=pk)
        carrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrdenList(APIView):
    def get(self, request):
        ordenes = Orden.objects.all()
        serializer = OrdenSerializer(ordenes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrdenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdenDetail(APIView):
    def get(self, request, pk):
        orden = Orden.objects.get(pk=pk)
        serializer = OrdenSerializer(orden)
        return Response(serializer.data)

    def put(self, request, pk):
        orden = Orden.objects.get(pk=pk)
        serializer = OrdenSerializer(orden, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        orden = Orden.objects.get(pk=pk)
        orden.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)