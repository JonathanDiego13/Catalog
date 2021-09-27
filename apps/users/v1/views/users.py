# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

#Model
from apps.users.models import User

#Permissions
from apps.users.v1.permissions import IsAdmin

# Serializers
from apps.users.v1.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
)


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """ User view set.
        Handle sign up and login
    """

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.action in ['login']:
            permissions = [AllowAny]
        elif self.action in ['signup', 'retrieve','update', 'destroy']:
            permissions = [IsAuthenticated, IsAdmin]
        else:
            permissions = [IsAuthenticated]

        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""

        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
