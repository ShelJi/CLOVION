from django.db import models

class blogData(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField()
    img = models.ImageField( upload_to="img", null= True)
    blogId = models.CharField( max_length=3, null = True)
    
class blogUser(models.Model):
    userName = models.CharField( max_length=10)
    userPassword = models.CharField( max_length=10)
    blogId = models.CharField( max_length=3, null = True)