from django.shortcuts import  render ,redirect
from django.contrib.auth.models import User
from django.dispatch import Signal, receiver
from django.db.models.signals import post_save
from signalapp.models import Profile,Product
from django.contrib import messages
from django.views import View
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView ,UpdateView , DeleteView
from django.views.generic.base import TemplateView

# Create your views here.


## SIGNAL
my_signal = Signal(providing_args= ['name'])

## SIGNAL FUNCTION
@receiver(post_save , sender = User )
def Prof(sender , instance , created , **kwargs):
    if created:
        prof = Profile.objects.create(user = instance)
        prof.save()
        print(instance,created,kwargs,sender)



def home(request):
    return render(request , "home.html")

def msgs(request):
    messages.info(request , "This is info messages")
    messages.success(request , "This is success messages")
    messages.warning(request , "This is warning messages")
    return render(request , 'msgs.html')

## FUNCTION BASED VIEW

# def user_login(request):
#     if request.method == "POST":
#         fisrtName = request.POST.get('fname')
#         lastName = request.POST.get('lname')
#         userName = request.POST.get('uname')
#         Email = request.POST.get("email")
#         user = User.objects.create(first_name = fisrtName , last_name = lastName , username = userName , email = Email)
#         user.save()
#         return redirect("/")
#         print(request.POST)
#     return render(request , 'login.html')


## CLASS BASED VIEW

class Login(View):
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

class UserList(ListView):
    model = User
    
class ProfileList(ListView):
    model = Profile
    context_object_name = "prof"

class ProductList(ListView):
    model = Product
    context_object_name = "prod"

    

## DETAIL VIEW  

class ProfileDetail(DetailView):
    model = Profile
    context_object_name = "prof"
    template_name = 'signalapp/Profile.html'
   
    def get_context_data(self, *args ,**kwargs) :
        context =  super().get_context_data(*args , **kwargs)
        context['AllProfiles'] = self.model.objects.all()
        return context

class ProductDetail(DetailView):
    model = Product
    context_object_name = "prod"
    template_name = 'signalapp/Productview.html'
   
    def get_context_data(self, *args ,**kwargs) :
        context =  super().get_context_data(*args , **kwargs)
        context['AllProduct'] = self.model.objects.all()
        return context


## CREATE VIEW

class AddProduct(CreateView):
    model = Product
    fields = ['name' , 'price', 'cat']
    template_name = 'signalapp/AddProduct.html'
    success_url = '/thank'
    
class Thankyou(TemplateView):
    template_name = "signalapp/thank.html"


## UPDATE VIEW

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name' , 'price', 'cat']
    template_name = 'signalapp/UpdateProduct.html'
    success_url = '/thankforupdate'

class Thankforupdate(TemplateView):
    template_name = "signalapp/thankforupdate.html"

## DELETE VIEW 

class DeletePorduct(DeleteView):
    model = Product
    success_url = "/Addproduct"