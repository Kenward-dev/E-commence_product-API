from rest_framework import generics, status
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from products.permissions import IsAdmin, IsSeller
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from products.permissions import IsAdmin

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdmin]

class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        order_id = self.kwargs['pk'] 
        return get_object_or_404(Order, id=order_id, user=self.request.user)


class SellerOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsSeller]

    def get_queryset(self):
        return Order.objects.filter(product__seller=self.request.user)

class OrderItemReturnView(generics.UpdateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdmin]

    def get_object(self):
        order_id = self.kwargs['order_id']
        item_id = self.kwargs['item_id']
        order = get_object_or_404(Order, id=order_id, user=self.request.user)
        return get_object_or_404(OrderItem, id=item_id, order=order)

    def update(self, request, *args, **kwargs):
        order_item = self.get_object()
        
        if hasattr(order_item, 'is_returned') and order_item.is_returned:
            return Response({"detail": "This item has already been returned."}, status=status.HTTP_400_BAD_REQUEST)

        # Increase the stock quantity
        product = order_item.product
        product.stock_quantity += order_item.quantity
        product.save()

        # Mark the item as returned
        if hasattr(order_item, 'is_returned'):
            order_item.is_returned = True
            order_item.save()

        serializer = self.get_serializer(order_item)
        return Response(serializer.data)

# class OrderItemListView(generics.ListAPIView):
#     serializer_class = OrderItemSerializer

#     def get_queryset(self):
#         return OrderItem.objects.filter(order__user=self.request.user)