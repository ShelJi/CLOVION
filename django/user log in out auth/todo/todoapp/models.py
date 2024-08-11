from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
    task = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)