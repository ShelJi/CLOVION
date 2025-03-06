import icecream as ic
# ic.disable

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import *

# giving and getting datas without DB
@api_view(["GET","POST"])
def index(request):
    if request.method == "GET":
        course = {"name":"python", 
                  "students":10,
                  "list":["hello","world"]
                }
        return Response(course)
    
    elif request.method == "POST":
        datas = request.data
        ic(datas)
        return Response(datas)
    
# giving and getting datas with DB
@api_view(["GET","POST","PUT","PATCH","DELETE"])
def person(request):
    if request.method == "GET":
        datas = Person.objects.all()
        ser = PersonSer(datas, many=True)
        return Response(ser.data)
    
    elif request.method == "POST":
        ser = PersonSer(data = request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
    elif request.method == "PUT":
        person = Person.objects.get(pk=request.data.get("id"))
        ser = PersonSer(data = request.data, instance=person)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
    elif request.method == "PATCH":
        person = Person.objects.get(pk=request.data.get("id"))
        ser = PersonSer(instance= person, data= request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
    elif request.method == "DELETE":
        person = Person.objects.get(pk=request.data.get("id"))
        person.delete()
        return Response()
    
# using only GET and POST method doing all 5 functions without foreignkey
@api_view(["GET","POST"])
def personSimple(request):
    if request.method == "GET":
        person = Person.objects.get(pk=request.data.get("id"))
        ser = PersonSer(person)
        return Response(ser.data)
        
    elif request.method == "POST":
        person = Person.objects.get(pk=request.data.get("id"))
        # ser = PersonSer(request.data) # POST Method Function
        # ser = PersonSer(data=request.data, instance=person) # PUT Method Function
        ser = PersonSer(data=request.data, instance=person, partial=True) # PATCH Method function
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
        
# using only GET and POST method doing all 5 functions with foreignkey model
@api_view(["GET","POST"])
def personForeign(request):
    if request.method == "GET":
        person = Person.objects.all()
        ser = PersonSer(person, many=True)
        return Response(ser.data)
        
    elif request.method == "POST":
        ser = PersonSer(data=request.data) 
        if ser.is_valid():
            # ser.validated_data["book"] = Book.objects.get(book=request.data["book"]) # ser should be modified
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
        
        # other method is by adding primarykeyrelatedfield in serializer

############################ CBV ##############################

from rest_framework.views import APIView
from rest_framework import viewsets

class IndexView(APIView):
    def get(self, request):
        return Response({'message':'This is a GET method'})
    
    def post(self, request):
        return Response({'message': "This is a POST method"})
    
    def put(self, request):
        return Response({'message': "This is a PUT method"})
    
    def patch(self, request):
        return Response({'message': "This is a PATCH method"})
    
    def delete(self, request):
        return Response({'message': "This is a DELETE method"})

# viewsets requires router
class IndexViewsets(viewsets.ModelViewSet):
    serializer_class = PersonSer 
    queryset = Person.objects.all()
