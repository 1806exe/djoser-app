from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """User model"""
    username_validator = UnicodeUsernameValidator()
    email = models.EmailField(
        _('email address'),
        max_length=180,
        unique=True
    )

    username = models.CharField(max_length=20, blank=True,
                                null=True, default='')
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

