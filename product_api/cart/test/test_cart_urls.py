from django.test import TestCase
from django.urls import reverse, resolve
from cart.views import CartRetrieveView, CartItemListCreateView, CartItemRetrieveUpdateDestroyView, CheckoutView

class TestCartUrls(TestCase):
    def test_cart_detail_url(self):
        url = reverse('cart-detail')
        self.assertEqual(resolve(url).func.view_class, CartRetrieveView)

    def test_cart_item_list_create_url(self):
        url = reverse('cart-item-list-create')
        self.assertEqual(resolve(url).func.view_class, CartItemListCreateView)

    def test_cart_item_detail_url(self):
        url = reverse('cart-item-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, CartItemRetrieveUpdateDestroyView)

    def test_checkout_url(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func.view_class, CheckoutView)