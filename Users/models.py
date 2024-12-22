from django.db import models
from django.contrib.auth.models import User
from Products.models import Producto
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """Crea y devuelve un usuario con un correo electrónico y contraseña."""
        if not email:
            raise ValueError('El correo electrónico debe ser proporcionado')
        if not username:
            raise ValueError('El nombre de usuario debe ser proporcionado')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)  # Almacena la contraseña de forma segura
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """Crea y devuelve un superusuario con un correo electrónico y contraseña."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        # Verificar si el superusuario ya existe
        if self.model.objects.filter(email=email).exists() or self.model.objects.filter(username=username).exists():
            raise ValidationError('Un superusuario con este correo electrónico o nombre de usuario ya existe.')

        return self.create_user(email, username, password, **extra_fields)

class CustomUser (AbstractBaseUser , PermissionsMixin):
    """Modelo de usuario personalizado."""
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    objects = CustomUserManager()  # Asigna el CustomUser  Manager
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'  # Usa el correo electrónico como el campo único para autenticación
    REQUIRED_FIELDS = ['username']  # Campos requeridos al crear un superusuario

    def __str__(self):
        return self.email  # Representación del usuario por su correo electrónico
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"