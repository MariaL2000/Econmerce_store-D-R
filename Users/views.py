from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from Products.models import Producto
from .models import Order
from .serializers import CustomUserSerializer, LoginSerializer, OrderSerializer
#from django.views.generic import TemplateView esto para cuando hagas el index. o home


class AuthView(generics.GenericAPIView):
    """Vista para registrar un nuevo usuario o iniciar sesión."""
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Verifica si se está registrando o iniciando sesión
        if 'register' in request.data:
            return self.register(request)
        elif 'login' in request.data:
            return self.login(request)
        else:
            return Response({"detail": "Acción no válida."}, status=status.HTTP_400_BAD_REQUEST)

    def register(self, request):
        """Método para registrar un nuevo usuario."""
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'message': 'Usuario registrado exitosamente.'
        }, status=status.HTTP_201_CREATED)

    def login(self, request):
        """Método para iniciar sesión de un usuario."""
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

class PurchaseView(generics.GenericAPIView):
    """Vista para manejar la compra de productos."""
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        # Verifica si el producto existe y está en stock
        try:
            product = Producto.objects.get(id=product_id)
            if product.stock < quantity:
                return Response({"detail": "Producto no disponible en la cantidad solicitada."}, status=status.HTTP_400_BAD_REQUEST)
        except Producto.DoesNotExist:
            return Response({"detail": "Producto no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Procesa el pago (aquí puedes integrar tu lógica de pago)
        # Suponiendo que el pago es exitoso, reducimos el stock del producto
        product.stock -= quantity
        product.save()

        # Crea una orden
        order = Order.objects.create(user=request.user, product=product, quantity=quantity)
        order_serializer = OrderSerializer(order)

        return Response({
            "detail": "Compra realizada exitosamente.",
            "order": order_serializer.data
        }, status=status.HTTP_200_OK)
    
