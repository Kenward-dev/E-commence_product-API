from rest_framework import generics, permissions
from rest_framework.permissions import SAFE_METHODS
from .models import Review
from .serializers import ReviewSerializer
from django.shortcuts import get_object_or_404
from products.permissions import IsAdmin

class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_id'])

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, product_id=self.kwargs['product_id'])

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Short-circuit if this is a Swagger schema generation request
        if getattr(self, 'swagger_fake_view', False):
            return Review.objects.none()  # return an empty queryset
        
        
        queryset = Review.objects.filter(product_id=self.kwargs['product_id'])
        if self.request.method not in SAFE_METHODS:
            queryset = queryset.filter(user=self.request.user)
        return queryset
    
    def get_object(self):
        # Short-circuit if this is a Swagger schema generation request
        if getattr(self, 'swagger_fake_view', False):
            return None  # return None to prevent issues during schema generation
        
        return get_object_or_404(Review, product_id=self.kwargs['product_id'], pk=self.kwargs['pk'])


# Admin can delete any review
class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdmin]