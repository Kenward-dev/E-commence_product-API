from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/profile/', views.ProfileRetrieveUpdateAPIView.as_view(), name='profile-update'),
    path('user/delete/', views.DeleteAccountView.as_view(), name='delete-account'),
    path('api/v1/auth/admin/users/', views.AdminUserListView.as_view(), name='admin-user-list'),  
    path('api/v1/auth/admin/users/<int:id>/', views.AdminUserManagementView.as_view(), name='admin-user-detail'),
]
