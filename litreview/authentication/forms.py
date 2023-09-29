from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import SetPasswordForm
from .validators import ContainsLetterValidator, ContainsNumberValidator, Password1Password2
from django.contrib.auth.views import PasswordResetForm


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder': 'Pseudo'}),
                               error_messages={
                                   'unique': "Ce nom d'utilisateur est déjà utilisé. Veuillez en choisir un autre."})

    email = forms.CharField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                            error_messages={
                                'unique':
                                    "Cet email existe déjà dans notre base de données."})

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe'}))

    def clean_password2(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')

        validator1 = ContainsLetterValidator()
        validator1.validate(password1)

        validator2 = ContainsNumberValidator()
        validator2.validate(password1)

        password2 = cleaned_data.get('password2')
        validator3 = Password1Password2()
        validator3.validate(password1, password2)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


# forms.py
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Pseudo'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Nouveau mot de passe'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirmer le nouveau mot de passe'}))

    def clean_new_password2(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        validator1 = ContainsLetterValidator()
        validator1.validate(new_password1)

        validator2 = ContainsNumberValidator()
        validator2.validate(new_password1)

        validator3 = Password1Password2()
        validator3.validate(new_password1, new_password2)
