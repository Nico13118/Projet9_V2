from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, error_messages={
        'unique': "Ce nom d'utilisateur est déjà utilisé"})
    email = models.EmailField(max_length=100, unique=True, error_messages={
        'unique': "Cet email existe déjà dans notre base de données"})
    password = models.CharField(blank=False, max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
