from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class PublicUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "avatar")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.USER   # force USER role for public signup
        if commit:
            user.save()
        return user


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "role", "avatar")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "role", "avatar")
