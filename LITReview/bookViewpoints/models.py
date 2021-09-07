from subscribers.models import App_users
from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField, TextField

# Create your models here.

class Book(models.Model):
    title = CharField(max_length=30)
    img_url = CharField(max_length=35)

    def average_rating(self):
        # calcul la note moyenne du livre
        # book_number = pk du livre(self)
        # n = 0
        # total = 0
        # pour chaque ticket_ref dans les objets de Review:
        #   si le ticket_review vaut book_number:
        #       rajouter 1 à n
        #       rajouter le rating de l'objet Review à total
        # avg_rating = t / n pour n différent de 0
        # renvoyer avg_rating
        pass

class Ticket(models.Model):
    ticket_date = DateTimeField('publié le ')
    description = TextField()
    user_name = models.ForeignKey(App_users, on_delete=models.CASCADE)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)

class Review(models.Model):
    title = title = CharField(max_length=30)
    comment = TextField()
    Rating = IntegerField(default=-1)
    pub_date = DateTimeField('publié le ')
    user_name = models.ForeignKey(App_users, on_delete=models.CASCADE)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    ticket_ref = models.ForeignKey(Ticket, on_delete=models.CASCADE)
