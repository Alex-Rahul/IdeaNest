from django.urls import path
from . import views

urlpatterns = [
    path("", views.users_home, name="users_home"),  
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
]
