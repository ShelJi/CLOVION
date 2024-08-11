from django import forms
from django.contrib.auth.models import User
from todoapp.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

class LogForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ["task"]
        
class StatusForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ["status"]