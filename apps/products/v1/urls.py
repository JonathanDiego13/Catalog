"""Users URLs."""

# Django
from django.urls import include, path

# Views
from rest_framework.routers import DefaultRouter

from apps.products.v1.views import products as products_api_v1

route = DefaultRouter()
route.register(r'products/v1', products_api_v1.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(route.urls))
]
