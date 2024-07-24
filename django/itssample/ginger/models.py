from django.db import models

# Create your models here.

class employeeData(models.Model):
    img = models.ImageField( upload_to="img", null = True)
    name = models.CharField(max_length = 20)
    age = models.IntegerField(null = True)
    position = models.TextField(null = True)
    gender = models.CharField(max_length = 10)
    salary = models.IntegerField(null = True)
    password = models.CharField(max_length = 10, null = True)
    