from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Pseudo'}))
    email = forms.CharField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe'}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Pseudo'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))


