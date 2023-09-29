from django.db import models
from django.contrib.auth.models import AbstractUser


# litreview\authentication\models.py
class User(AbstractUser):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(blank=False, max_length=150)
    is_active = models.BooleanField(default=True)

    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='follower')

    def __str__(self):
        return self.username
