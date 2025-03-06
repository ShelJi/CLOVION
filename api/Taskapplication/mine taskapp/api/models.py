from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
    task_user = models.ForeignKey( User, on_delete=models.CASCADE)
    task_name = models.CharField( max_length=100)
    task_created = models.DateTimeField( auto_now_add=True)
    task_status = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.task_user} - {self.task_name}"
    
class TaskReview(models.Model):
    task_name = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    review = models.CharField( max_length=50)
    
    def __str__(self):
        return self.task_name