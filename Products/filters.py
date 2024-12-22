from django_filters import ModelChoiceFilter
import django_filters
from .models import Categoria, Producto  # Asegúrate de tener un modelo de categoría

class ProductoFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter(field_name="price", lookup_expr='exact')
    price_range = django_filters.RangeFilter(field_name="price")
    category = ModelChoiceFilter(queryset=Categoria.objects.all())

    class Meta:
        model = Producto
        fields = ['price', 'price_range', 'category']