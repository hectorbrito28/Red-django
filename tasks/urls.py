from django.urls import path
from . import views as v


urlpatterns = [
    path("Signup/",v.signupview,name="signup"),
    path("Home/",v.home,name="Home"),
    path("Logout/",v.logoutview,name="Logout"),
    path("Signin/",v.signin,name="Signin"),
    path("tasks/",v.taskview,name="TASK"),
    path("Update/",v.savetask,name="SAVE"),
    path("delete/",v.deletetask,name="DEL"),
    path("detailtask/", v.taskdetail,name="DETAIL")
]