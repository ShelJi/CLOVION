from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets

from sample.models import *
from sample.serializer import *


@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def index(request):
    
    data = {'message' : 'hello', 'hey' : 'default'}
    if request.method == 'GET':
        return Response(data)
    elif request.method == 'POST':
        print(request.data)
        return Response(f'{request.data} hello')
    elif request.method == 'PUT':
        return Response(f'{request.data} PUT method')
    elif request.method == 'PATCH':
        return Response(f'{request.data} PATCH method')

#it only works for table without foreign key
#for table with foreign key use the post method detail in CBV in this FBV
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def home(request):
    if request.method == 'GET':
        # data = PersonModel.objects.all()
        data = PersonModel.objects.filter(kidney__isnull = False)
        serializer = PersonSerializer(data, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        data = request.data
        obj = PersonModel.objects.get(id= data['id'])
        serializer = PersonSerializer(obj, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        data = request.data
        obj = PersonModel.objects.get(id= data['id'])
        serializer = PersonSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        data = request.data
        obj = PersonModel.objects.get(id = data['id'])
        obj.delete()
        return Response(status=status.HTTP_200_OK)

class NewViews(APIView):
    def get(self, request):
        data = PersonModel.objects.all()
        # data = PersonModel.objects.filter(kidney__isnull = False)
        serializer = PersonSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        val = KidneyModel.objects.get(type = request.data['type'])
        serializer = PersonModel.objects.create(name=request.data['name'],
                                                age = request.data['age'],
                                                empty = request.data['empty'],
                                                type = request.data['type'],
                                                kidney = val)
        serializer.save()
        return Response("data=serializer.data")
    
    # def put(self, request):
    #     val = 
    
    def patch(self, request):
        data = request.data
        obj = PersonModel.objects.get(id= data['id'])
        serializer = PersonSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        obj = PersonModel.objects.get(id = data['id'])
        obj.delete()
        return Response(status=status.HTTP_200_OK)

class NewViewset(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()