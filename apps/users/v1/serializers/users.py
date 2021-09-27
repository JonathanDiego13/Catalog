"""Users serializers."""

# Django
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from apps.users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'is_admin'
        )


class UserSignUpSerializer(serializers.Serializer):
    """ User sign up serialiazer.
        Handle sign up data validation and user creation.
    """

    phone_regex = RegexValidator(
        regex=r'\d{10}$',
        message='Phone number must be entered in the format: 9999999999. Up to 10 digits allowed.'
    )

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    first_name = serializers.CharField(
        min_length=2,
        max_length=30
    )

    last_name = serializers.CharField(
        min_length=2,
        max_length=30
    )

    phone_number = serializers.CharField(
        validators=[
            phone_regex,
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    is_admin =  serializers.BooleanField()

    password = serializers.CharField(
        min_length=8,
        max_length=64
    )

    password_confirmation = serializers.CharField(
        min_length=8,
        max_length=64
    )

    def validate(self, data):
        """Verify passwords match."""

        password = data['password']
        password_confirmaton = data['password_confirmation']

        if password != password_confirmaton:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(password)

        return data

    def create(self, data):
        """Handle user and profile creation."""

        data.pop('password_confirmation')
        user = User.objects.create_user(**data)#is_admin=False
        return user


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.
    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(
        min_length=8,
        max_length=64
    )

    def validate(self, data):
        """Check credentials."""

        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not True:
            raise serializers.ValidationError('Account is not active yet :(')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve new token."""

        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
