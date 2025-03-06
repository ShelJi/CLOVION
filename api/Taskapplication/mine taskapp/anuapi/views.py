from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from anuapi.serializers import *
from anuapi.models import Student

# Create your views here.
@api_view(['POST'])
def studentcreate(request):
    print(request.data)
    data={
        'name':request.data['name'],
        'place':request.data["place"]
    }
    serializer=Studentserilizer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data)
    return Response("data saved")
   
@api_view(["GET"])
def studentdisplay(request):
    data=Student.objects.all()
    serializer = Studentlistserilizer(data, many=True)
    return Response(data=   serializer.data)
   
        