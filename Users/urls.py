from django.urls import path
from .views import AuthView, PurchaseView

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'), 
    path('purchase/', PurchaseView.as_view(), name='purchase'), 
]