from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from subscribers.models import UserFollows


class UserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']


class AuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            print("Le compte existe, mais il est inactif.")


class FollowForm(ModelForm):
    class Meta:
        model = UserFollows
        fields = ['followed_user']
        labels = {"followed_user": "Cherchez un utilisateur à suivre"}
