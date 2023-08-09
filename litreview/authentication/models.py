from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'
    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )
    username = models.CharField(max_length=100, unique=True, error_messages={
        'unique': "Ce nom d'utilisateur est déjà utilisé"})
    email = models.EmailField(max_length=100, unique=True, error_messages={
        'unique': "Cet email existe déjà dans notre base de données"})
    password = models.CharField(blank=False, max_length=150)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

    follows = models.ManyToManyField(
        'self',
        limit_choices_to={'role': CREATOR},
        symmetrical=False,
        verbose_name='suit',
    )

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
