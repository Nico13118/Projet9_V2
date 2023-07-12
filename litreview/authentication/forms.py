from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'Adresse email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'})
    )

