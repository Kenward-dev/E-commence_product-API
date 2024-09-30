from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/update/<int:pk>/', views.OrderUpdateView.as_view(), name='order-update'),
    path('orders/seller/', views.SellerOrderListView.as_view(), name='seller-order-list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:order_id>/items/<int:item_id>/return/', views.OrderItemReturnView.as_view(), name='order-item-return'),
    # path('order-items/', OrderItemListView.as_view(), name='order-item-list'),
]