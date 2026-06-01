from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        USER = "USER", "User"
        ADMIN = "ADMIN", "Admin"
        SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.USER)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def save(self, *args, **kwargs):
        # Sync role with staff/superuser flags
        if self.role == self.Role.SUPER_ADMIN:
            self.is_staff = True
            self.is_superuser = True
        elif self.role == self.Role.ADMIN:
            self.is_staff = True
            self.is_superuser = False
        else:
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="user_profile")
    extra_field_user = models.CharField(max_length=100, blank=True)


class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="admin_profile")
    department = models.CharField(max_length=100, blank=True)


class SuperAdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="superadmin_profile")
    system_access_level = models.CharField(max_length=100, blank=True)


# Auto-create correct profile when user is created
@receiver(post_save, sender=CustomUser)
def create_role_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == CustomUser.Role.USER:
            UserProfile.objects.create(user=instance)
        elif instance.role == CustomUser.Role.ADMIN:
            AdminProfile.objects.create(user=instance)
        elif instance.role == CustomUser.Role.SUPER_ADMIN:
            SuperAdminProfile.objects.create(user=instance)


# ACID-safe merge function
def merge_user_data(user_id):
    with transaction.atomic():
        user = CustomUser.objects.select_for_update().get(id=user_id)

        if user.role == CustomUser.Role.USER:
            profile = getattr(user, "user_profile", None)
        elif user.role == CustomUser.Role.ADMIN:
            profile = getattr(user, "admin_profile", None)
        elif user.role == CustomUser.Role.SUPER_ADMIN:
            profile = getattr(user, "superadmin_profile", None)
        else:
            profile = None

        return {
            "username": user.username,
            "role": user.role,
            "details": profile.__dict__ if profile else {}
        }
