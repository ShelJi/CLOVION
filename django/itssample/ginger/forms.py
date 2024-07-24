from django.forms import ModelForm
from ginger.models import employeeData

class employeeDataForm(ModelForm):
    class Meta:
        model = employeeData
        fields = ["name", "age", "position", "gender", "salary", "img"]
        
class LoginCheck(ModelForm):
    class Meta:
        model = employeeData
        fields = ["name", "password"]