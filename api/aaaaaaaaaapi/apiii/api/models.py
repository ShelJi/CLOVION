from django.db import models

class Book(models.Model):
    book = models.CharField(max_length=50, null=True, blank=True)
    book_name = models.CharField( max_length=50)
    returned = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.book

class Person(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    
    # class Meta:
    #     ordering = ["age"]

    def __str__(self) -> str:
        return self.name