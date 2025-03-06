from api.models import *
from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
        widgets ={
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ["task_name"]