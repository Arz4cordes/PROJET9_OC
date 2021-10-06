from django.forms import ModelForm
from bookViewpoints.models import Review, Ticket
from subscribers.models import UserFollows

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'body',
                  'rating']
        labels = {
            "headline": "Titre de la critique",
            "body": "Commentaires",
            "rating": "Note (sur 5)"
        }

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {"title": "Titre du livre",
                  "description": "Description du livre"}


class FollowForm(ModelForm):
    class Meta:
        model = UserFollows
        fields = ['followed_user']
        labels = {"followed_user": "Cherchez un utilisateur à suivre"}
