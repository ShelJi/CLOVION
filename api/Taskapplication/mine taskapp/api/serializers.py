from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskModel   
        fields = ["task_name"]