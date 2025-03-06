from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from api.models import *
from tasks.forms import *
from django.urls import reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/taskweb/login/')
def homeview(request):
    data = TaskModel.objects.filter(task_user_id=request.user.id)
    return render(request, 'index.html', {"datas": data})


def signupview(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,"account created successfully")
            login(request, user)
            return redirect(reverse("home"))
        else:
            messages.error(request, "Invalid input")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("home"))
            else:
                messages.error(request, "user does not exist")
        else:
            messages.error(request, "Invalid Data")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

def logoutview(request):
    logout(request)
    return redirect(reverse("login"))

def taskview(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            formupdate = form.save(commit=False)
            formupdate.task_user = request.user 
            formupdate.save()
        else:
            messages.error(request, "Invalid data")
        
    return redirect(reverse("home"))

def editview(request, id):
    if TaskModel.objects.filter(id = id):
        data = get_object_or_404(TaskModel, id = id)
        
        if data.task_status:
            data.task_status = False
        else:
            data.task_status = True
            
        data.save()
    return redirect(reverse("home"))
    
def delview(request, id):
    data = get_object_or_404(TaskModel, id = id)    
    data.delete()
    return redirect(reverse("home"))
