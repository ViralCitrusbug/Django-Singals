from django.shortcuts import render
from django.contrib.auth.models import User
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from signalapp.models import Profile
from django.contrib import messages
from django.views import View

# Create your views here.


## SIGNAL

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
        messages.success(request , "Your Account Has been Successfully Created")
        return render(request , "login.html")
        


#3 SIGNAL FUNCTION
@receiver(post_save , sender = User )
def Prof(sender , instance , created , **kwargs):
    if created:
        prof = Profile.objects.create(user = instance)
        prof.save()
        print(instance,created,kwargs,sender)


def Msgs(request):
    messages.info(request , "This is info messages")
    messages.success(request , "This is success messages")
    messages.warning(request , "This is warning messages")
    return render(request , 'msgs.html')