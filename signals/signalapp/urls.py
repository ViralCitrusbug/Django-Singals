"""signals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from collections import UserList
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from .views import Msgs, login,user_list,Profile_detail,Profile_list,AddProduct,Thankyou
urlpatterns = [
    path('', views.home , name = "home"),
    # path('login', views.user_login , name = "login")
    path('login', login.as_view() , name = "login"),
    path('messages', views.Msgs , name = "msgs"),
    path('user_list', user_list.as_view(), name ='user_list'),
    path('profile_list' , Profile_list.as_view(), name="profile"),
    path("profile/<int:pk>", Profile_detail.as_view(), name ='profile_detail'),
    path('Addproduct', AddProduct.as_view(), name = "addproduct"),
    path('thank' , Thankyou.as_view() , name = "thank")
]

