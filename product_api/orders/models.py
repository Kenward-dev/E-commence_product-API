from django.db import models
from django.conf import settings
from products.models import Product

class Order(models.Model):
    PENDING = 'P'
    COMPLETED = 'C'
    CANCELLED = 'X'
    RETURNED = 'R'
    
    ORDER_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
        (RETURNED, 'Returned'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES, default=PENDING)
    
    def __str__(self):
        return f"Order {self.id} - {self.get_status_display()}"
    
    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    @property
    def item_price(self):
        return self.product.price
    
    @property
    def total_price(self):
        return self.product.price * self.quantity