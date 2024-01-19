from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=500)
    done = models.BooleanField(default=False)