from rest_framework import serializers
from .models import Cart, CartItem
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        required=True,
        help_text="Select a product to add to cart"
    )
    quantity = serializers.IntegerField(
        min_value=1,
        default=1,
        help_text="Enter the quantity (default is 1)"
    )
    # ADDED: New total_price field
    total_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True,
        help_text="Total price for this cart item"
    )

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price', 'created_at', 'updated_at']

# from rest_framework import serializers
# from .models import Cart, CartItem
# from products.serializers import ProductSerializer

# class CartItemSerializer(serializers.ModelSerializer):
#     product = ProductSerializer(read_only=True)
#     total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

#     class Meta:
#         model = CartItem
#         fields = ['id', 'product', 'quantity', 'total_price']

