from django.forms import ModelForm
from shop.models import *

class ProductDataForm(ModelForm):
    class Meta:
        model = ProductData
        fields = ["image", "product_name", "description", 
                  "discount_price", "actual_price", "stock", 
                  "trending", "category"]
        
class UserDataForm(ModelForm):
    class Meta:
        model = UserData
        fields = ["name", "password"]
        
class BuyerDataForm(ModelForm):
    class Meta:
        model = buyerData
        fields = "__all__"