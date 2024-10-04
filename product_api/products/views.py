from rest_framework import generics, filters
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSeller
from .pagination import ProductPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category__name']
    ordering_fields = ['price', 'name', 'created_at']
    ordering = ['-created_at']  # Default ordering
    pagination_class = ProductPagination

    def get_queryset(self):
        # Start with all in-stock products
        queryset = Product.objects.filter(stock_quantity__gt=0)
        
        # Apply role-based filtering for seller
        if self.request.user.is_seller() and not self.request.user.is_admin():
            # Sellers see only their products
            queryset = queryset.filter(seller=self.request.user)
        # Admins and regular authenticated users see all products
        
        # Apply price range filters if provided
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=float(min_price))
        if max_price:
            queryset = queryset.filter(price__lte=float(max_price))
        
        # Apply search filter if provided
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(category__name__icontains=search_query)
            )
        
        return queryset.distinct()
    
# Seller can add and delete products
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSeller]
    
    def perform_create(self, serializer):
        # Set the seller field to the current authenticated user
        serializer.save(seller=self.request.user)

# Seller can only list their own products and update them
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSeller]

    def get_queryset(self):
        # Ensure the seller can only update their own products
        return Product.objects.filter(seller=self.request.user)
    
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSeller]
    
    def get_queryset(self):
        # Ensure the seller can only delete their own products
        return Product.objects.filter(seller=self.request.user)
    

        
        ##################################
# UpdateAPIView to GenericAPIView with PATCH method
#from rest_framework.response import Response
# class ProductUpdateView(generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsSeller]

#     def get_queryset(self):
#         # Ensure the seller can only update their own products
#         return Product.objects.filter(seller=self.request.user)
    
#     # Added patch method for partial updates
#     def patch(self, request, *args, **kwargs):
#         instance = self.get_object()
#         # partial=True allows partial updates
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)