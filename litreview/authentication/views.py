from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm, CustomSetPasswordForm
from django.contrib.auth.views import PasswordResetConfirmView


class SignUpPage(View):
    form_class = forms.SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'authentication/signup.html', context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        return render(request, 'authentication/signup.html', context={'form': form})


def registration_success(request):
    return render(request, 'success.html')


def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')


def password_reset_done(request):
    return render(request, 'password_reset_done.html')


def logout_user(request):
    logout(request)
    return redirect('login')


# views.py
class LoginPageView(View):
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'authentication/login.html', context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('flow')
        message = 'Identifiant ou mot de passe invalide !!'
        return render(request, 'authentication/login.html', context={'form': form, 'message': message})


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'password_reset_form.html'
    email_template_name = 'password_reset_email.html'
    token_generator = default_token_generator
    success_url = reverse_lazy("password_reset_done")
    from_email = settings.DEFAULT_FROM_EMAIL
    subject_template_name = "password_reset_subject.txt"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
