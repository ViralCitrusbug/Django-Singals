
import profile
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from signalapp.models import Profile
from django.views import View
# Create your views here.

my_signal = Signal(providing_args= ['name'])

def home(request):
    return render(request , "home.html")


## FUNCTION BASED VIEW

# def user_login(request):
#     if request.method == "POST":
#         fisrtName = request.POST.get('fname')
#         lastName = request.POST.get('lname')
#         userName = request.POST.get('uname')
#         Email = request.POST.get("email")
#         user = User.objects.create(first_name = fisrtName , last_name = lastName , username = userName , email = Email)
#         user.save()
#         print(request.POST)
#     return render(request , 'login.html')


## CLASS BASED VIEW

class login(View):
    def get(self , request):
        return render(request , "login.html")
    def post(self ,request):
        fisrtName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        userName = request.POST.get('uname')
        Email = request.POST.get("email")
        user = User.objects.create(first_name = fisrtName , last_name = lastName , username = userName , email = Email)
        user.save()
        a = "ViralPatel"
        c ={
            "a" : a
        }
        return render(request , "login.html",c)
        

@receiver(post_save , sender = User )
def Prof(sender , instance , created , **kwargs):
    if created:
        prof = Profile.objects.create(user = instance)
