from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class User(AbstractUser):
    pass

class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                            on_delete=models.CASCADE,
                            related_name='following')
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    related_name='followed_by')
    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'followed_user'], name='abonnement'),
                       ]
