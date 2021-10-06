from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from django.db.models.fields import CharField, DateTimeField, \
                                    PositiveSmallIntegerField, TextField, \
                                    BooleanField

# Create your models here.


class Ticket(models.Model):
    title = CharField(max_length=128, default='Titre du ticket')
    time_created = DateTimeField(auto_now_add=True)
    description = TextField(max_length=2048, blank=True)
    answer = BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/photos/%Y/%m/%d', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def time_display(self):
        ticket_date = f"le {self.time_created.day}/"
        ticket_date += f"{self.time_created.month}/"
        ticket_date += f"{self.time_created.year} "
        ticket_date += f"à {self.time_created.hour}h"
        ticket_date += f"{self.time_created.minute}min "
        return ticket_date


class Review(models.Model):
    headline = CharField(max_length=128, default='Titre de la critique')
    body = TextField(max_length=8192, blank=True)
    rating = PositiveSmallIntegerField(default=0,
             validators=[MinValueValidator(0),MaxValueValidator(5)])
    time_created = DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)

    def time_display(self):
        review_date = f"le {self.time_created.day}/"
        review_date += f"{self.time_created.month}/"
        review_date += f"{self.time_created.year} "
        review_date += f"à {self.time_created.hour}h"
        review_date += f"{self.time_created.minute}min "
        return review_date