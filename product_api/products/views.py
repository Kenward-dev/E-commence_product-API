from rest_framework import generics, filters
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSeller
from .pagination import ProductPagination
from rest_framework.exceptions import PermissionDenied
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
        
        # Apply additional filters only if provided in the request
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=float(min_price))
        if max_price:
            queryset = queryset.filter(price__lte=float(max_price))
        
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
# class ProductListCreateView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
        
#         serializer.save(seller=request.user)
#         response = {'message': 'product added successfully', 'product': serializer.data}
#         return Response(response, status=status.HTTP_201_CREATED)
        

# class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'id'