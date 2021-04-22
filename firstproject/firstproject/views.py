from django.http import HttpResponse
from django.shortcuts import  render

def stud_register(request):
    return render(request,"student/studlogin.html")

def student_login(request):
    return HttpResponse("<h1>welcome to student login</h1>")

def view_timetable(request):
    return  HttpResponse("<h1>timing</h1>")

def post_feedback(request):
    return  HttpResponse("<h1>post your feedbacks</h1>")