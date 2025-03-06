from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from task_list.models import Task
from .serializers import TaskSerializer, empty_get_print_ser, empty_get_print_ser_many

@api_view(["GET"])
def empty_get_print(request):
    # Create a dictionary to represent your data
    datas = {"name": "hello"}  # Use a dictionary with the expected key

    # Initialize the serializer with the data
    ser = empty_get_print_ser(data=datas)

    # Check if the data is valid
    if ser.is_valid():
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def empty_get_print_many(request):
    # Create a dictionary to represent your data
    datas = {"name": "hello","place":"engaiyo"}  # Use a dictionary with the expected key

    # Initialize the serializer with the data
    ser = empty_get_print_ser_many(data=datas)

    # Check if the data is valid
    if ser.is_valid():
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def empty_get_print_simple(request):
    datas = "hello"  

    return Response(datas, status=status.HTTP_200_OK)

@api_view(["GET"])
def empty_get_print_simple_many(request):
    datas = ["hello","world"]

    return Response(datas, status=status.HTTP_200_OK)

@api_view(["POST"])
def empty_post(request):
    datas = request.data
    return Response(datas)

@api_view(["POST"])
def task_post(request):
    ser = TaskSerializer(request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_200_OK)
    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

###########################################################

@api_view(["GET"])
def all_data_view(request):
    datas = Task.objects.all()
    ser = TaskSerializer(datas, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def task_user(request):
    datas = Task.objects.filter(id= 5)
    ser = TaskSerializer(datas, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)

