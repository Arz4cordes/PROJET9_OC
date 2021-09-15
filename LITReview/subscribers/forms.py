from django.forms import ModelForm
from django.conf import settings

# ou bien:
# from django.contrib.auth.models import AbstractUser
# class User(AbstractUser):
#    full_name = models.CharField(max_length=50)
#    connected = True
# USER: django.contrib.auth.models.User

#class ConnectionForm(ModelForm):
#    class Meta:
#        model = settings.AUTH_USER_MODEL
#        fields = ['username', 'password']