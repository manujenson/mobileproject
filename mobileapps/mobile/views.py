from django.shortcuts import render,redirect
from mobile.forms import brandcreateform,mobilecreateform,orderform
from .models import Brands,Mobile,Orders
from .forms import userregform
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout

# Create your views here.
def admin_permission_required(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request)
    return wrapper

def admin_permission_required_id(func):
    def wrapper(request,id):
        if not request.user.is_superuser:
            return redirect("errorpage")
        else:
            return func(request,id)
    return wrapper

@admin_permission_required
def brand_view(request):

    brands = Brands.objects.all()
    form=brandcreateform()
    context={}
    context["brands"] = brands
    context["form"]=form
    if request.method == "POST":
        form = brandcreateform(request.POST)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("brandview")
    return render(request,"mobile/bndcreate.html",context)


def errorpg(request):
    return render(request, "mobile/errorpage.html")

@admin_permission_required_id
def brand_del(request,id):
    brand=Brands.objects.get(id=id)
    brand.delete()
    return redirect("brandview")

@admin_permission_required_id
def brand_update(request,id):
    brand=Brands.objects.get(id=id)
    form = brandcreateform()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = brandcreateform(request.POST,instance=brand)
        context["form"] = form
        form.save()

        return redirect("brandview")
    return render(request, "mobile/bndupdate.html", context)


def create_mobile(request):
    form=mobilecreateform()
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=mobilecreateform(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("createmobile")
    return render(request, "mobile/mobilecreate.html", context)

def list_mobiles(request):
    mobiles=Mobile.objects.all()
    context = {}
    context["mobiles"] =mobiles
    return render(request, "mobile/listmobiles.html", context)

def mobile_detail(request,id):
    mobile=Mobile.objects.get(id=id)
    context = {}
    context["mobile"] = mobile
    return render(request, "mobile/mobiledetail.html", context)

def user_reg(request):
    form=userregform()
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=userregform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            form=userregform(request.POST)
            context["form"] = form
            return render(request, "mobile/userreg.html", context)

    return render(request, "mobile/userreg.html", context)

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password = request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("listmobiles")
        else:
            return render(request, "mobile/login.html")

    return render(request, "mobile/login.html")

def user_logout(request):
    logout(request)
    return redirect("userlogin")

def order(request,id):
    product=Mobile.objects.get(id=id)
    username=request.user
    form=orderform(initial={'user':request.user,"product":product})
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cart")
        else:
            form=orderform(request.POST)
            context["form"] = form
            return render(request, "mobile/order.html", context)
    return render(request, "mobile/order.html",context)

def cart_details(request):
    username=request.user
    orders = Orders.objects.filter(user=username)
    print(orders)
    context = {}
    context["orders"] = orders
    return render(request, "mobile/cartdetails.html", context)

def order_del(request,id):
    order=Orders.objects.get(id=id)
    order.delete()
    return redirect("cart")

def order_view(request,id):

    order = Orders.objects.get(id=id)
    form= orderform()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = orderform(request.POST, instance=order)
        context["form"] = form
        form.save()

        return render(request,"mobile/orderview.html",context)
    return render(request, "mobile/orderview.html", context)


