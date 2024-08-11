from django.db import models

category_choice = [("Mobile", "mobile"),
                   ("Headset", "headset"),
                   ("Watch", "watch"),
                   ("Battery", "battery"),
                   ("Case", "case"),
                   ("Electronics", "electronics")]

class UserData(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)  
    
    def __str__(self):
        return self.name

class ProductData(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    discount_price = models.IntegerField()
    actual_price = models.IntegerField()
    stock = models.IntegerField()
    trending = models.BooleanField(default=False)
    category = models.CharField( max_length=50, choices=category_choice, default="Electronics")

    def __str__(self):
        return self.product_name
    
    
class buyerData(models.Model):
    name = models.CharField( max_length=50)
    password = models.CharField( max_length=10)

class Cart(models.Model):
    user = models.ForeignKey(buyerData, on_delete=models.CASCADE)
    productId = models.TextField()    
    