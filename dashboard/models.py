from django.db import models

class DashboardWidget(models.Model):
    name = models.CharField(max_length=100)

class DashboardLayout(models.Model):
    layout_name = models.CharField(max_length=100)

class DashboardAccess(models.Model):
    role = models.CharField(max_length=50)
