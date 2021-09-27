from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = ('email','username', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin', 'created', 'modified')
