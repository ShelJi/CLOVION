from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import TaskSerializer,UserSerializer
from api.models import Tasks
from django.contrib.auth.models import User



from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from rest_framework import authentication,permissions
# Create your views here.


# locahost:8000/tasks/

class TaskView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Tasks.objects.all() #queryset
        serializer=TaskSerializer(qs,many=True) #deserialization
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=TaskSerializer(data=request.data)    #serialization
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
# localhost:8000/tasks/1
class TaskDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Tasks.objects.get(id=id)
        serializer=TaskSerializer(qs,many=False)
        return Response(data=serializer.data)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get('id')
        Tasks.objects.get(id=id).delete()
        return Response(data='deleted')

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        obj=Tasks.objects.get(id=id)
        serializer=TaskSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



    
class TaskViewSet(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Tasks.objects.all()
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Tasks.objects.get(id=id)
        serializer=TaskSerializer(qs,many=False)
        return Response(data=serializer.data)
       
    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Tasks.objects.get(id=id)
        serializer=TaskSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Tasks.objects.get(id=id).destroy()
        return Response(data='destroy')


class TaskmodelViewsetView(ModelViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    serializer_class=TaskSerializer
    queryset=Tasks.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        qs=Tasks.objects.filter(user=request.user)
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data)
 
    def create(self, request, *args, **kwargs):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(User=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# completed task only display(method:get,detail:false or true)
    @action(methods=["GET"],detail=False)
    def finished_tasks(self,request,*args,**kwargs):
        qs=Tasks.objects.filter(status=True)
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data) 
    # localhost:8000/api/v1/tasks/pending_tasks/
    @action(methods=["GET"],detail=False)
    def pending_tasks(self,request,*args,**kwargs):
        qs=Tasks.objects.filter(status=False)
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data)
# localhost:800/api/v1/tasks/1/mark_as_done/
    @action(methods=["POST"],detail=True)
    def mark_as_done(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Tasks.objects.filter(id=id).update(status=True)
        return Response(data="status updated")


class UsersView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all() 



    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            usr=User.objects.create_user(**serializer.validated_data)
            serializer=UserSerializer(usr,many=False)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
