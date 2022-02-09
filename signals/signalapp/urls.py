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
from .views import msgs, Login,UserList,ProfileDetail,ProfileList,AddProduct,Thankyou,ProductUpdate,Thankforupdate,DeletePorduct,ProductList,ProductDetail
urlpatterns = [
    path('', views.home , name = "home"),
    # path('login', views.user_login , name = "login")
    path('login', Login.as_view() , name = "login"),
    path('messages', views.msgs , name = "msgs"),
    path('user-list', UserList.as_view(), name ='user_list'),
    path('profile/profile-list' , ProfileList.as_view(), name="profile"),
    path('product/product-list' , ProductList.as_view(), name="product"),
    path("profile/<int:pk>", ProfileDetail.as_view(), name ='profile_detail'),
    path("product/<int:pk>", ProductDetail.as_view(), name ='Product_detail'),
    path('product/Addproduct', AddProduct.as_view(), name = "addproduct"),
    path('product/<int:pk>/update', ProductUpdate.as_view(), name = "updateproduct"),
    path('thank' , Thankyou.as_view() , name = "thank"),
    path('thankforupdate' , Thankforupdate.as_view() , name = "thankforupdate"),
    path('product/<int:pk>/delete', DeletePorduct.as_view(), name = "deleteproduct")
]

