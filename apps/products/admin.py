"""Products admin."""

# Django
from django.contrib import admin

# Models
from apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin."""

    list_display = (
        'name',
        'sku',
        'price',
        'brand',
    )

    search_fields = (
        'name',
        'sku'
        'brand'
    )

    list_filter = (
        'brand',
    )
