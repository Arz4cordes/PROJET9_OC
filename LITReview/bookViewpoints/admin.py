from django.contrib import admin

from .models import Book, Ticket, Review

admin.site.register(Book)
admin.site.register(Ticket)
admin.site.register(Review)
