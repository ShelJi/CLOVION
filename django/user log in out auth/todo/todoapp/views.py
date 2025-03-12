from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages

from todoapp.form import *

class HomeView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request):
        form = TaskForm()
        tasks = TaskModel.objects.filter(user = request.user)
        # tasks = None
        return render(request, "index.html", {"title": "DoTo",
                                              "tasks": tasks,
                                              "form": form})
    
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "task added")
            return redirect(reverse("home"))
            
        return render(request, "index.html", {"form":form})

class SignUpView(View): 
    def get(self, request):
        form = UserForm()
        return render(request, "log/log.html", {"topic": "Sign Up",
                                                "title": "Sign Up",
                                                "form": form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request, "New User Created")
            return redirect(reverse("login"))
        else:
            messages.error(request, "Failed to create user. Retry")

        return render(request, "log/log.html", {"title": "Sign Up",
                                                "topic": "Sign Up",
                                                "form": form})
    
class LoginView(View):
    def get(self, request):
        form = LogForm()
        return render(request, "log/log.html", {"title": "Login",
                                                "topic": "Login",
                                                "form": form})
    
    def post(self, request):
        form = LogForm(request.POST)
        if form.is_valid():
            user = authenticate(request, 
                                username=form.cleaned_data.get("username"), 
                                password=form.cleaned_data.get("password"))
            
            if user is not None:
                login(request, user)
                return redirect(reverse("home"))
            else:
                messages.error(request, "Invalid User")
                
        return render(request, "log/log.html", {"title": "Login",
                                                "topic": "Login",
                                                "form": form})
        
class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.error(request, "Logged Out")
        else:
            messages.error(request, "Not Logged In")
        
        return redirect(reverse("login"))
    
class EditView(LoginRequiredMixin, View):
    login_url = "/login/"
    
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(TaskModel, id = kwargs.get("id"))
        print(kwargs)
        task.status = not task.status
        task.save()
        return redirect(reverse("home"))
    
class DeleteView(LoginRequiredMixin, View):
    login_url = "/login/"
    
    def get(self, request, *args, **kwargs):
        TaskModel.objects.get(id = kwargs.get("id")).delete()
        return redirect(reverse("home"))
    
def register_view(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request, "New User Created")
            return redirect(reverse("login"))
        else:
            messages.error(request, "Failed to create user. Retry")

        return render(request, "log/log.html", {"title": "Sign Up",
                                                "topic": "Sign Up",
                                                "form": form})

    return render(request, "log/log.html", {"topic": "Sign Up",
                                            "title": "Sign Up",
                                            "form": form})

def login_view(request):
    form = LogForm()
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            user = authenticate(request, 
                                username=form.cleaned_data.get("username"), 
                                password=form.cleaned_data.get("password"))
            
            if user is not None:
                login(request, user)
                return redirect(reverse("home"))
            else:
                messages.error(request, "Invalid User")
                
        return render(request, "log/log.html", {"title": "Login",
                                                "topic": "Login",
                                                "form": form})
       
def logout_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            logout(request)
            messages.error(request, "Logged Out")
        else:
            messages.error(request, "Not Logged In")
        
        return redirect(reverse("login"))

def home_view(request):
    form = TaskForm()
    tasks = TaskModel.objects.filter(user = request.user)
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, "task added")
            return redirect(reverse("home"))
            
        return render(request, "index.html", {"form":form})

    return render(request, "index.html", {"title": "DoTo",
                                            "tasks": tasks,
                                            "form": form})