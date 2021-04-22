from django.shortcuts import render

# Create your views here.
from .forms import bookcreateform,bookupdateform
from django.shortcuts import render,redirect
from .models import Book
from .forms import userregform,loginform
from  django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView,TemplateView
from django.urls import reverse_lazy

def book_create(request):
    form=bookcreateform()
    context={}
    context["form"]=form
    books=Book.objects.all()
    context["books"]=books
    if request.method=="POST":
        form=bookcreateform(request.POST)
        if form.is_valid():
            form.save()


            print("book object saved")
            return redirect("create")
        else:
            form = bookcreateform(request.POST)
            context["form"] =form
            return render(request, "book/bookcreate.html", context)

    return render(request,"book/bookcreate.html",context)

def book_delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect("create")

def book_view(request,id):
    book=Book.objects.get(id=id)
    context = {}
    context["book"] =book
    return render(request, "book/bookdetail.html", context)

def book_update(request,pk):
    book=Book.objects.get(id=pk)
    form=bookupdateform(instance=book)
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=bookupdateform(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("create")
    return render(request, "book/bookedit.html", context)


def registration(request):
    form=userregform()
    context = {}
    context["form"]=form
    if request.method == "POST":
        form = userregform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"book/login.html")
        else:
            form = userregform(request.POST)
            context["form"] = form
            return render(request, "book/registration.html", context)

    return render(request, "book/registration.html", context)


def login_view(request):
    form=loginform()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                print("login success")
                login(request,user)
                return redirect("create")
            else:
                print("failed")
                return render(request,"book/login.html")

    return render(request, "book/login.html", context)

#create
#detailview
#updateview
#deleteview

#listing of all books
class Books(TemplateView):
    model = Book
    template_name =  "book/bookcreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        books=self.model.objects.all()
        self.context["books"]=books
        return render(request,self.template_name,self.context)


class bookcreate(TemplateView):
    model = Book
    form_class = bookcreateform
    template_name = "book/bookcreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        self.context["form"] = self.form_class()
        return render(request,self.template_name,self.context)
    def post(self,request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clslist")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)

class bookupdateview(TemplateView):
    model = Book
    form_class = bookcreateform
    template_name = "book/bookedit.html"
    context={}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):

        #kwargs={id:7}
        book=self.get_object(kwargs["pk"])
        form=self.form_class(instance=book)
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        book=self.get_object(kwargs["pk"])
        form=self.form_class(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("clslist")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)


class bookdetail(TemplateView):
    model = Book
    template_name = "book/bookdetail.html"
    context={}
    def get(self,request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs["pk"])
        self.context["book"]=book
        return render(request,self.template_name,self.context)

class bookdelete(TemplateView):
    model = Book

    def get(self,request, *args, **kwargs):
        book=self.model.objects.get(id=kwargs["pk"])
        book.delete()
        return redirect("clslist")