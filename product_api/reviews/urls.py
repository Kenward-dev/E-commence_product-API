from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('product/<int:product_id>/reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review-delete'),
]
