# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from cart.models import Cart, CartItem
# from cart.serializers import CartSerializer, CartItemSerializer
# from products.models import Product

# User = get_user_model()

# class TestCartSerializer(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='testuser', email='test@google.com', password='testpassword123')
#         self.cart = Cart.objects.create(user=self.user)
#         self.product = Product.objects.create(name='Test Product', price=10.00, stock_quantity=5)
#         self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

#     def test_cart_serializer(self):
#         serializer = CartSerializer(instance=self.cart)
#         self.assertIn('id', serializer.data)
#         self.assertIn('user', serializer.data)
#         self.assertIn('items', serializer.data)
#         self.assertIn('total_price', serializer.data)
#         self.assertEqual(serializer.data['total_price'], '20.00')

# class TestCartItemSerializer(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', email='test@google.com', password='testpassword123')
#         self.cart = Cart.objects.create(user=self.user)
#         self.product = Product.objects.create(name='Test Product', price=10.00, stock_quantity=5)
#         self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

#     def test_cart_item_serializer(self):
#         serializer = CartItemSerializer(instance=self.cart_item)
#         self.assertIn('id', serializer.data)
#         self.assertIn('product', serializer.data)
#         self.assertIn('quantity', serializer.data)
#         self.assertIn('total_price', serializer.data)
#         self.assertEqual(serializer.data['total_price'], '20.00')