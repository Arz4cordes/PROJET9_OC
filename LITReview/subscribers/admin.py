from django.contrib import admin

from .models import UserFollows
# from django.contrib.auth.admin import UserAdmin
# class MyUserAdmin(UserAdmin):

admin.site.register(UserFollows)
