#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Utilities
from catalog.utils.models import CatalogModel


class User(CatalogModel, AbstractUser):
    """Extending django user model, using a custom model extending AbstractUser"""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']
    phone_regex = RegexValidator(
        regex=r'\d{10}$',
        message='Phone number must be entered in the format: 9999999999. Up to 10 digits allowed.'
    )

    email = models.EmailField(
        'email_address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exits'
        }
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=10,
        unique=True,
        error_messages = {
            'unique': 'A user with that email already exits'
        }
    )

    is_admin = models.BooleanField(
        'admin user',
        default=True,
        help_text = (
            'Help easily distinguish user and perform queries. ',
            'Admins are the main type of user.'
        )
    )

    def __str__(self):
        return self.username
