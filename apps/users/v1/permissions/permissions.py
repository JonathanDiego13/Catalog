"""User permissions."""

#Django REST Framework
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        is_admin = getattr(request.user, 'is_admin')
        return is_admin
