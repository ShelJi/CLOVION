from django.db import models

# from django.contrib.auth.models import User 

# Create your models here.
class Wow_model(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    
    img = models.ImageField(upload_to = "img", null = True) #null = True should be used on after added values
