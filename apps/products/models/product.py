"""Products model."""

#Django
from django.db import models

#Utilities
from apps.utils.models import CatalogModel
from .product_user_relationship import ProductUserRelationship


class Product(CatalogModel):

    name = models.CharField(
        'product name',
        max_length=40,
    )
    sku = models.CharField(
        'product name',
        max_length=12,
        unique=True,
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    brand = models.CharField(
        'product name',
        max_length=40,
    )
    is_public = models.BooleanField(
        'product',
        default=True,
        help_text = (
            'Help easily distinguish product and perform queries.',
        )
    )

    product_user_relationship = models.ManyToManyField(
        'users.User',
        through='products.ProductUserRelationship',
        through_fields=('product', 'user')
    )

    def __str__(self):
        return self.name

    def update_times_queried_number(self, user):
        user_id = getattr(user, 'id')
        product_id = getattr(self, 'id')

        prod_user_rs = ProductUserRelationship.objects.filter(user=user_id, product=product_id)
        for purs in prod_user_rs:
            times_queried_number = getattr(purs, 'times_queried_number')

        if prod_user_rs:
            times_queried_number += 1
            prod_user_rs.update(times_queried_number=times_queried_number)
        else:
            ProductUserRelationship.objects.create(
                user=user,
                product=self,
                times_queried_number=1
            )

    class Meta(CatalogModel.Meta):
        ordering = ['-name']
