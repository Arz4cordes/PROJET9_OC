from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class App_users(models.Model):
    full_name = models.CharField(max_length=30)
    user_password = CharField(max_length=25)
    connected = False

    def __str__(self):
        return self.full_name

class Follower(models.Model):
    followed_by = models.ForeignKey(App_users, on_delete=models.CASCADE)
