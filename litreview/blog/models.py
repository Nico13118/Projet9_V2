from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Photo(models.Model):
    objects = models.Manager()
    image = models.ImageField(on_delete=models.CASCADE)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


# Créer un ticket (Demander une critique)
class Ticket(models.Model):
    objects = models.Manager()
    photo = models.ForeignKey(Photo, null=True, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    response = models.CharField(max_length=1, default='0')


# Créer une critique (En réponse ou Pas en réponse à un ticket)
class Review(models.Model):
    objects = models.Manager()
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
