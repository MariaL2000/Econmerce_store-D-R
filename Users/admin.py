from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser 

class CustomUserAdmin(UserAdmin):
    # Especifica los campos que se mostrarán en el panel de administración
    model = CustomUser 
    list_display = ('email', 'username', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('email', 'username')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    # Para que el campo de contraseña se muestre correctamente
    def save_model(self, request, obj, form, change):
        if not change:  # Si es un nuevo usuario
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

# Registra el modelo en el admin
admin.site.register(CustomUser , CustomUserAdmin)


# Register your models here.
