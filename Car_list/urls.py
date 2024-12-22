from django.urls import path
from .views import CarritoList, CarritoDetail, OrdenList, OrdenDetail


app_name = 'Car_list'

urlpatterns = [
    path('carritos/', CarritoList.as_view(), name='carrito-list'),
    path('carritos/<int:pk>/', CarritoDetail.as_view(), name='carrito-detail'),
    path('ordenes/', OrdenList.as_view(), name='orden-list'),
    path('ordenes/<int:pk>/', OrdenDetail.as_view(), name='orden-detail'),
]

