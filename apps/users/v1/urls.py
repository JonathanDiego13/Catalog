"""Users URLs."""

# Django
from django.urls import include, path

# Views
from rest_framework.routers import DefaultRouter

from apps.users.v1.views import users as user_api_v1

route = DefaultRouter()
route.register(r'users/v1', user_api_v1.UserViewSet, basename='users')

urlpatterns = [
    path('', include(route.urls))
]
