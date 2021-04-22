from django.shortcuts import render
#createyour views here.


from django.http import HttpResponse
from django.shortcuts import render
#
# def stud_register(request):
#     return render(request,"student/studlogin.html")
#
# def registration(request):
#     name=request.POST.get("name")
#     email=request.POST.get("email")
#     course=request.POST.get("crse")
#     print(name,course,email)
#     return render(request, "student/studlogin.html")
#
# def student_login(request):
#     return HttpResponse("<h1>welcome to student login</h1>")
#
# def view_timetable(request):
#     return  HttpResponse("<h1>timing</h1>")
#
# def post_feedback(request):
#     return  HttpResponse("<h1>post your feedbacks</h1>")
from student.forms import StudentRegistrationForm,studentloginform

def registration(request):
    form=StudentRegistrationForm()
    context={}
    context["form"]=form

    if request.method=="POST":
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("name")
            email=form.cleaned_data.get("email")
            phone=form.cleaned_data.get("phone")
            print(name,"=>",email,"=>",phone)
            return render(request, "student/studentregistration.html", context)

    return render(request,"student/studentregistration.html",context)

def login_view(request):

     form=studentloginform()
     context={}
     context["form"]=form
     if request.method == "POST":
         form = studentloginform(request.POST)
         if form.is_valid():
             username = form.cleaned_data.get("username")
             password = form.cleaned_data.get("password")
             print(username,",",password)

             return render(request,"student/studlogin.html",context)

     return render(request,"student/studlogin.html",context)
