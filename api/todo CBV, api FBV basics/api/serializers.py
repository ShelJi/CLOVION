from rest_framework import serializers
from task_list.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'complete', 'user']

class empty_get_print_ser(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    
class empty_get_print_ser_many(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    place = serializers.CharField(max_length=100)
    