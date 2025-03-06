from rest_framework import serializers
from anuapi.models import Student


class Studentserilizer(serializers.Serializer):
    name=serializers.CharField()
    place=serializers.CharField()
    
    def create(self,data):
        return Student.objects.create(
            name=data['name'],
            place=data["place"]
        )
        
class Studentlistserilizer(serializers.Serializer):
    name=serializers.CharField()
    place=serializers.CharField()