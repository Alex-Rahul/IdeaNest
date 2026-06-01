from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=200)

class ReportCategory(models.Model):
    name = models.CharField(max_length=100)

class ReportLog(models.Model):
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
