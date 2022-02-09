from turtle import pos
from django.contrib import admin
from signalapp.models import Profile,Post,products

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(products)