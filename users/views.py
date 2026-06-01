from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import PublicUserCreationForm
from django.http import HttpResponse
from .models import CustomUser

def register(request):
    if request.method == "POST":
        form = PublicUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = PublicUserCreationForm()
    return render(request, "users/register.html", {"form": form})

def users_home(request):
    return HttpResponse("Welcome to the Users section of IdeaNest.")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = CustomUser.objects.filter(email=email).first()
        user = None
        if user_obj:
            user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            login(request, user)
            if user.role == CustomUser.Role.SUPER_ADMIN:
                return redirect("/admin/")
            elif user.role == CustomUser.Role.ADMIN:
                return redirect("reports")
            else:
                return redirect("dashboard")
        else:
            return render(request, "users/login.html", {"error": "Invalid email or password"})

    return render(request, "users/login.html")
