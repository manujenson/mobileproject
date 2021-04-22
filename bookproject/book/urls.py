
from django.contrib import admin
from django.urls import path
from .views import book_create,book_delete,book_view,book_update,registration,login_view,bookupdateview,bookdetail,bookdelete

from .views import Books,bookcreate
urlpatterns = [
path("create",book_create,name="create"),
    path("delete/<int:id>",book_delete,name="delete"),
    path("view/<int:id>",book_view,name="detail"),
    path("edit/<int:pk>",book_update,name="edit"),
    path("register",registration,name="register"),
    path("login",login_view,name="logsin"),
    path("clslist",Books.as_view(),name="clslist"),
    path("clscreate",bookcreate.as_view(),name="clscreate"),
    path("clsupdate/<int:pk>",bookupdateview.as_view(),name="clsupdate"),
    path("clsdetail/<int:pk>",bookdetail.as_view(),name="clsbookdetail"),
    path("clsdelete/<int:pk>",bookdelete.as_view(),name="clsdelete")
]
