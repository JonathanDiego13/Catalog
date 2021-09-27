"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    path('', include(('apps.users.v1.urls', 'users'), namespace='users')),
    path('', include(('apps.products.v1.urls', 'products'), namespace='products'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
