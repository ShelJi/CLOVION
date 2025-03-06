from rest_framework import serializers
from sample.models import *

class KidneySerializer(serializers.ModelSerializer):
    class Meta:
        model = KidneyModel
        exclude = ['id']

class PersonSerializer(serializers.ModelSerializer):
    # kidney = KidneySerializer()
    class Meta:
        model = PersonModel
        fields = '__all__'
        depth = 2
        
    def validate_age(self, val):
        if val <= 18 : 
            raise serializers.ValidationError("Age should be greater than 18")
        return val
    
    # def validate(self, data):
    #     if data['age'] <= 18 : 
    #         raise serializers.ValidationError("Age should be greater than 18")
    #     return data
    ### PATCH Method Gives ERROR  when changing data without age form field in this second method of validation
    
