# from django.forms import ModelForm
from hello.models import Wow_model
from django import forms

from django.contrib.auth.models import User

class Wow_form(forms.ModelForm):
    class Meta:
        model = Wow_model
        fields = "__all__"
        # fields = ["name", "age"]

class User_auth(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
        }
        
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))