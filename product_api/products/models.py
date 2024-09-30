from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    image_url = models.URLField(max_length=200, null=True, blank=True)
    category = TaggableManager()
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def decrease_stock(self, quantity):
        """
        Decrease the stock quantity of the product.
        Raises ValueError if there's not enough stock.
        """
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            self.save()
        else:
            raise ValueError("Not enough stock available")

    def increase_stock(self, quantity):
        """
        Increase the stock quantity of the product.
        """
        self.stock_quantity += quantity
        self.save()