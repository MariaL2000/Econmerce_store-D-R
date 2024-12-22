from django.db import models

CATEGORY_CHOICES=(
    ('Cl', 'Clothes'),
    ('Ac','Accesories'),
    ('El','Electronics'),
    ('Sp','Sports'),
    ('Bk','Books'),
    ('Fd','Foods')
    )

# Modelo para almacenar la categoría de los productos
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para almacenar los productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_descuento=models.FloatField(null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/')
    cantidad_stock = models.IntegerField()
    categoria = models.CharField(choices= CATEGORY_CHOICES,max_length=2)

    def __str__(self):
        return self.nombre

    def actualizar_stock(self, cantidad):
        self.cantidad_stock -= cantidad
        self.save()

