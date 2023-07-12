from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=False, max_length=150, unique=True)
    username = models.CharField(blank=False, max_length=150, unique=True)
    password = models.CharField(blank=False, max_length=150)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    