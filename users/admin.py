from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile, AdminProfile, SuperAdminProfile
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "role", "is_staff", "is_superuser")
    list_filter = ("role", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", "avatar")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "avatar")}),
    )

# Profile admins with useful list displays
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "extra_field_user")
    search_fields = ("user__username", "user__email")


@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "department")
    search_fields = ("user__username", "user__email")


@admin.register(SuperAdminProfile)
class SuperAdminProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "system_access_level")
    search_fields = ("user__username", "user__email")


# Register CustomUser with its custom admin
admin.site.register(CustomUser, CustomUserAdmin)
