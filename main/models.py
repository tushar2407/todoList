from django.db import models

# Create your models here.
class Task(models.Model):
    work=models.CharField(max_length=256)