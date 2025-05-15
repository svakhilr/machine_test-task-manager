from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    SUPER_ADMIN = 'super_admin'
    ADMIN = 'admin'
    USER = 'user'
    
    CATEGORY_CHOICES = (
        (SUPER_ADMIN, 'Super-Admin'),
        (ADMIN, 'Admin'),
        (USER, 'User'),
    )

    
    username = models.CharField(unique=True)
    name = models.CharField(max_length=100,null=True)
    role = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username