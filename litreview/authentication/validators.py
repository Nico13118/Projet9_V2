from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password1, user=None):
        if not any(char.isalpha() for char in password1):
            raise ValidationError('Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule!',
                                  code='password_no_letters')


class ContainsNumberValidator:
    def validate(self, password1, user=None):
        if not any(char.isdigit() for char in password1):
            raise ValidationError('Le mot de passe doit contenir au moins un chiffre', code='password_no_numbers')


class Password1Password2:
    def validate(self, password1, password2, user=None):
        if password1 != password2:
            raise ValidationError('Les mots de passe ne sont pas identiques !', code='passwords_not_identical')
