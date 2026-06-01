from django.db import models

class Notification(models.Model):
    message = models.CharField(max_length=200)

class NotificationType(models.Model):
    name = models.CharField(max_length=100)

class NotificationLog(models.Model):
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
