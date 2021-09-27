# Django REST Framework
from rest_framework import mixins, viewsets

#Model
from apps.products.models import Product

# Serializers
from apps.products.v1.serializers import ProductModelSerializer


class ProductViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """ Product view set.
        Handle
    """

    serializer_class = ProductModelSerializer
    lookup_field = 'sku'

    def get_queryset(self):
        """Restrict list to public-only"""
        queryset = Product.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset
