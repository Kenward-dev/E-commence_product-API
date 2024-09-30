from django.urls import path
from .views import (
    CartRetrieveView, 
    CartItemListCreateView, 
    CartItemRetrieveUpdateDestroyView, 
    CheckoutView)

urlpatterns = [
    path('cart/', CartRetrieveView.as_view(), name='cart-detail'),
    path('cart/items/', CartItemListCreateView.as_view(), name='cart-item-list-create'),
    path('cart/items/<int:pk>/', CartItemRetrieveUpdateDestroyView.as_view(), name='cart-item-detail'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]