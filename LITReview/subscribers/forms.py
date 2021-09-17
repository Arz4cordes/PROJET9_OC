from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class ConnectionForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            "username": "Nom de l'utilisateur",
            "password": "Mot de passe"
        }

class PickyAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if user.id < 5:
            raise ValidationError(
                _("id inférieur à 5."),
                code='inactive',)