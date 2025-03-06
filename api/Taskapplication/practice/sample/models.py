from django.db import models

class KidneyModel(models.Model):
    count = models.IntegerField( null=True)
    type = models.CharField( max_length=50, null=True)
    
    def __str__(self) -> str:
        return self.type
    
class PersonModel(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField()
    empty = models.CharField( max_length=50)
    kidney = models.ForeignKey( KidneyModel, on_delete=models.CASCADE, null=True)
    type = models.CharField( max_length=50, null=True)
    
    def __str__(self) -> str:
        return self.name
    