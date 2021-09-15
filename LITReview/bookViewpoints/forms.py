from django import forms
from bookViewpoints.models import Review, Ticket

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'body',
                  'rating']
        labels = {
            "headline": "Titre de la critique",
            "body": "Commentaires",
            "rating": "Note (sur 5)"
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']
        labels = {"title": "Titre du livre",
                  "description": "Description du livre"}
