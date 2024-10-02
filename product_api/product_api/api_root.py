from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        # Auth endpoints
        'auth': {
            'register': reverse('register', request=request, format=format),
            'login': reverse('login', request=request, format=format),
            'token': reverse('token_obtain_pair', request=request, format=format),
            'token_refresh': reverse('token_refresh', request=request, format=format),
            'token_verify': reverse('token_verify', request=request, format=format),
            'user_profile': reverse('profile-update', request=request, format=format),
            'admin': {  
                'django_admin': reverse('admin:index', request=request, format=format),
                'users': {
                    'list': reverse('admin-user-list', request=request, format=format),
                    'detail': 'api/v1/auth/admin/users/<id>/',
                }
            },
        },
        # Product endpoints
        'products': {
            'list': reverse('product-list', request=request, format=format),
            'create': reverse('product-create', request=request, format=format),
            'update': 'api/v1/products/<id>/update/',
            'delete': 'api/v1/products/<id>/delete/',
        },
        # Cart endpoints
        'cart': {
            'detail': reverse('cart-detail', request=request, format=format),
            'items': reverse('cart-item-list-create', request=request, format=format),
            'item_detail': 'api/v1/cart/items/<id>/',
            'checkout': reverse('checkout', request=request, format=format),
        },
        # Order endpoints
        'orders': {
            'list': reverse('order-list', request=request, format=format),
            'seller_orders': reverse('seller-order-list', request=request, format=format),
            'update': 'api/v1/orders/update/<id>/',
            'detail': 'api/v1/orders/<id>/',
            'return_item': 'api/v1/orders/<order_id>/items/<item_id>/return/',
        },
        # Review endpoints
        'reviews': {
            'list_create': 'api/v1/product/<product_id>/reviews/',
            'detail': 'api/v1/product/<product_id>/reviews/<id>/',
            'delete': 'api/v1/reviews/<id>/delete/',
        },
        # API Documentation
        'documentation': {
            'swagger': reverse('schema-swagger-ui', request=request, format=format),
            'redoc': reverse('schema-redoc', request=request, format=format),
        },
    })