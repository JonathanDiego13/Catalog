"""ProductUserRelationship model."""

# Django
from django.db import models

# Utilities
from utils.models import CatalogModel


class ProductUserRelationship(CatalogModel):
    """ProductUserRelationship model.
    """

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
    )

    # Stats
    times_queried_number = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        """Return username and circle."""
        return '@{} at #{}'.format(
            self.user.username,
            self.product.sku
        )
