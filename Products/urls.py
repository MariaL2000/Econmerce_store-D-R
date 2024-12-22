from django.urls import path
from .views import ProductList, ProductDetail, ProductFilterList, ProductoListView

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('products/filter/', ProductFilterList.as_view(), name='product-filter-list'),
    path('products/list/', ProductoListView.as_view(), name='producto-list-view'),
]