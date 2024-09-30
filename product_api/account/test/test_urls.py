from django.test import TestCase
from django.urls import reverse, resolve
from account import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView, 
    TokenVerifyView
)

class TestUrls(TestCase):
    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, views.RegisterView)
    
    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, views.LoginView)
    
    def test_token_obtain_pair_resolves(self):
        url = reverse('token_obtain_pair')
        self.assertEqual(resolve(url).func.view_class, TokenObtainPairView)
        
    def test_token_refresh_resolves(self):
        url = reverse('token_refresh')
        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)
    
    def test_token_verify_resolves(self):
        url = reverse('token_verify')
        self.assertEqual(resolve(url).func.view_class, TokenVerifyView)
    
    def test_profile_update_resolves(self):
        url = reverse('profile-update')
        self.assertEqual(resolve(url).func.view_class, views.ProfileRetrieveUpdateAPIView)
    
    def test_url_names(self):
        self.assertEqual(reverse('register'), '/api/v1/auth/register/')
        self.assertEqual(reverse('login'), '/api/v1/auth/login/')
        self.assertEqual(reverse('token_obtain_pair'), '/api/v1/auth/token/')
        self.assertEqual(reverse('token_refresh'), '/api/v1/auth/token/refresh/')
        self.assertEqual(reverse('token_verify'), '/api/v1/auth/token/verify/')
        self.assertEqual(reverse('profile-update'), '/api/v1/auth/user/profile/')