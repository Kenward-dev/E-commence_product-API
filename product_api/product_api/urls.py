from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce-Product API",
        default_version='v1',
        description="API that allows the user to order products, track orders and check seamlessly",
        contact = openapi.Contact(
            name="Kenward Terhemba",                   
            email="codewithkenward@gmail.com",     
            projects="https://github.com/Kenward-dev"      
        )
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/', include_docs_urls(title='E-Commerce-Product API', permission_classes=[permissions.AllowAny])),
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('account.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('cart.urls')),
    path('api/v1/', include('orders.urls')),
    path('api/v1/', include('reviews.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/schema.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/schema.yaml/', schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
        path('api/schema/', get_schema_view(
        title="E-Commerce-Product API",
        description="API for all things E-Commerce",
        version="1.0.0",
        public=True,
        permission_classes=[permissions.AllowAny],
    ), name='openapi-schema'),
]
