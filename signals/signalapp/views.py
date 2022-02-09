from dataclasses import fields
from msilib.schema import SelfReg
from pyexpat import model
from venv import create
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from signalapp.models import Profile,products
from django.contrib import messages
from django.views import View
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

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
        

##  LIST VIEW   

class user_list(ListView):
    model = User
    
class Profile_list(ListView):
    model = Profile
    context_object_name = "prof"

    

## DETAIL VIEW  

class Profile_detail(DetailView):
    model = Profile
    context_object_name = "prof"
    template_name = 'signalapp/Profile.html'
   
    def get_context_data(self, *args ,**kwargs) :
        context =  super().get_context_data(*args , **kwargs)
        context['AllProfiles'] = self.model.objects.all()
        return context

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

## CREATE VIEW

class AddProduct(CreateView):
    model = products
    fields = ['name' , 'price', 'cat']
    template_name = 'signalapp/AddProduct.html'
    success_url = '/thank'
    
    
class Thankyou(TemplateView):
    template_name = "signalapp/thank.html"