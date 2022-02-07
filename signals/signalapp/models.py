from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save , pre_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12)

    def __str__(self) :
        return self.user.username

class Post(models.Model):
    post_user = models.CharField(max_length=120 , default="")

def save_post(sender , instance, created , **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_pre(sender, instance , **kwargs):
    print("Pre save Working")

post_save.connect(save_post , sender = Post)
pre_save.connect(save_pre , sender = Post)