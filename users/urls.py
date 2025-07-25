from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    path("", views.Home, name="home"),
    path("register/", views.RegisterView, name="register"),
    path("login/", views.LoginView, name="login"),
]