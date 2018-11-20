from django.urls import path
from .import views

urlpatterns = [
    path("",views.index, name= "index" ),
    path("author/<name>/",views.getauthor, name = "author"),
    path("artical/<int:id>",views.getsingle, name = "sigle_post"),
    path("topic/<name>/",views.gettopic, name = "topic"),
    path("login/",views.getlogin, name = "login"),
    path("logout/",views.getlogout,name="logout"),
    path("create/",views.getcreate, name= "create"),
    path("profile/",views.getprofile, name= "profile"),
    path("update/<int:id>",views.getupdate, name = "update"),
    path("delete/<int:id>",views.getdelete, name = "delete"),
    path("register/",views.getregister, name="register")

]