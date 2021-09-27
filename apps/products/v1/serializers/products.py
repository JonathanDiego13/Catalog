"""Users serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.products.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name',
            'sku',
            'price',
            'brand',
            'is_public'
        )
