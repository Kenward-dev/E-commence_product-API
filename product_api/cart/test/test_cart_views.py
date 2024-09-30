# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from rest_framework.test import APIClient
# from rest_framework import status
# from cart.models import Cart, CartItem
# from products.models import Product
# from orders.models import Order

# User = get_user_model()

# class TestCartViews(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(
#             username='testuser', 
#             email='test@google.com', 
#             password='testpassword123'
#             )
#         self.client.force_authenticate(user=self.user)
#         self.product = Product.objects.create(
#             name='Test Product', 
#             price=10.00, 
#             stock_quantity=5)

#     def test_cart_retrieve_view(self):
#         url = reverse('cart-detail')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('items', response.data)
#         self.assertIn('total_price', response.data)

#     def test_cart_item_list_create_view(self):
#         url = reverse('cart-item-list-create')
#         data = {'product': self.product.id, 'quantity': 2}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_cart_item_retrieve_update_destroy_view(self):
#         cart = Cart.objects.get(user=self.user)
#         cart_item = CartItem.objects.create(
#             cart=cart, 
#             product=self.product, 
#             quantity=1)
#         url = reverse('cart-item-detail', args=[cart_item.id])
        
#         # Test retrieve
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        
#         # Test update
#         response = self.client.patch(url, {'quantity': 3})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(CartItem.objects.get(id=cart_item.id).quantity, 3)
        
#         # Test destroy
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(CartItem.objects.filter(id=cart_item.id).exists())

#     def test_checkout_view(self):
#         cart = Cart.objects.get(user=self.user)
#         CartItem.objects.create(cart=cart, product=self.product, quantity=2)
#         url = reverse('checkout')
#         response = self.client.post(url)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertIn('order_id', response.data)
#         self.assertTrue(Order.objects.filter(user=self.user).exists())
#         self.assertEqual(CartItem.objects.filter(cart=cart).count(), 0)