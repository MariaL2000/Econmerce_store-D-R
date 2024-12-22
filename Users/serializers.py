from rest_framework import serializers
from .models import CustomUser ,Order
import re

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        if not value:
            raise serializers.ValidationError("El nombre de usuario es obligatorio.")
        if CustomUser .objects.filter(username=value).exists():
            raise serializers.ValidationError("El nombre de usuario ya está en uso.")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("El correo electrónico es obligatorio.")
        if CustomUser .objects.filter(email=value).exists():
            raise serializers.ValidationError("El correo electrónico ya está en uso.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise serializers.ValidationError("El correo electrónico no es válido.")
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise serializers.ValidationError("La contraseña debe contener al menos un carácter especial.")
        return value

    def create(self, validated_data):
        user = CustomUser (
            email=validated_data['email'],
            username=validated_data['username'],

        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if not CustomUser .objects.filter(email=email).exists():
            raise serializers.ValidationError("El correo electrónico no existe.")
        user = CustomUser .objects.get(email=email)
        if not user.check_password(password):
            raise serializers.ValidationError("La contraseña es incorrecta.")
        return attrs
    


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'