"""Products model."""

#Django
from django.db import models

#Utilities
from apps.utils.models import CatalogModel


class Product(CatalogModel):

    name = models.CharField('circle name', max_length=40)
    sku = models.CharField('circle name', max_length=12)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.CharField('circle name', max_length=40)

    def __str__(self):
        return self.name

    class Meta(CatalogModel.Meta):
        ordering = ['-name']
