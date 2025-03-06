from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.TextField()
    place=models.TextField()