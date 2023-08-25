from django import forms
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()


class PhotoForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = models.Photo
        fields = ['image']


class TicketForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label='Titre')
    description = forms.CharField(max_length=8192, label='Description')

    class Meta:
        model = models.Ticket
        fields = ['title', 'description']


class ReviewForm(forms.ModelForm):
    headline = forms.CharField(max_length=128, label='Titre')
    rating = forms.CheckboxInput()
    body = forms.CharField(max_length=8192, label='Commentaire')

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body', 'ticket']


# litreview\blog\forms.py
class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['following']
