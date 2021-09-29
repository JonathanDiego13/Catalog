# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

#Model
from apps.products.models import Product

#Permissions
from commons.permissions import IsAdmin

# Serializers
from apps.products.v1.serializers import ProductModelSerializer


class ProductViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """ Product view set.
        Handle
    """

    serializer_class = ProductModelSerializer
    lookup_field = 'sku'

    def get_permissions(self):
        if self.action in ['list']:
            permissions = [AllowAny]
        elif self.action in ['retrieve']:
            permissions = [IsAuthenticated]
        elif self.action in ['create', 'update', 'destroy']:
            permissions = [IsAuthenticated, IsAdmin]
        else:
            permissions = [IsAuthenticated]

        return [p() for p in permissions]

    def get_queryset(self):
        """Restrict list to public-only"""
        queryset = Product.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        response = super(ProductViewSet, self).retrieve(request, *args, *kwargs)

        is_admin = getattr(request.user, 'is_admin')
        if not is_admin:
            # Track of the number of times every single product is queried by an anonymous user
            product = Product.objects.get(sku=response.data['sku'])
            product.update_times_queried_number(request.user)

        return response

    def update(self, request, *args, **kwargs):
        response = super(ProductViewSet, self).update(request, *args, *kwargs)
        product = Product.objects.get(sku=response.data['sku'])
        product.send_notifications()
        return response
