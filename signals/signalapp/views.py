import email
import imp
from signal import signal
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save

from signalapp.models import Profile
# Create your views here.

my_signal = Signal(providing_args= ['name'])

def home(request):
    return HttpResponse("You are at Home")


def user_login(request):
    if request.method == "POST":
        fisrtName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        userName = request.POST.get('uname')
        Email = request.POST.get("email")
        user = User.objects.create(first_name = fisrtName , last_name = lastName , username = userName , email = Email)
        user.save()
        print(request.POST)


    return render(request , 'login.html')

@receiver(post_save , sender = User )
def Prof(sender , instance , created , **kwargs):
    if created:
        prof = Profile.objects.create(user = instance)
