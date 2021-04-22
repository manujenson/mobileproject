"""mobileapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import brand_view,create_mobile,list_mobiles,mobile_detail,user_reg,user_login,user_logout,order,cart_details,brand_del,brand_update,errorpg,order_del,order_view

urlpatterns = [
    path("error", errorpg, name="errorpage"),
    path("", lambda request: render(request, "mobile/index.html")),
    path("brands",brand_view,name="brandview"),
    path("brands/delete/<int:id>",brand_del,name="delete"),
    path("brands/edit/<int:id>",brand_update,name="edit"),
    path("mobiles",create_mobile,name="createmobile"),
    path("mobiles/list",list_mobiles,name="listmobiles"),
    path("mobile/detail/<int:id>",mobile_detail,name="detail"),
    path("mobiles/userregistration",user_reg,name="register"),
    path("mobile/userlogin",user_login,name="userlogin"),
    path("mobile/userlogout",user_logout,name="userlogout"),
    path("mobile/order/<int:id>",order,name="order"),
    path("mobile/cart",cart_details,name="cart"),
    path("mobile/cart/delt/<int:id>",order_del,name="delt"),
    path("mobile/cart/view/<int:id>",order_view,name="view")

]
