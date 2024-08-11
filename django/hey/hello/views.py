from django.shortcuts import render, redirect, reverse
from hello.forms import *
from hello.models import *

from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages


# decorator

def signin_required(fn):
    def wrapper_val(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse("signin"))

        return fn(request, *args, **kwargs)
    return wrapper_val



# Create your views here.
def indexPage(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        data = Wow_form(request.POST, request.FILES)
        
        if data.is_valid():
            data.save()
            return redirect("/display/")
        
    return render(request, "index.html")

# @signin_required
def displayPage(request):
    values = Wow_model.objects.all()
    context = {"value" : values}
    return render(request, "display.html", context)

def displayDelete(request, id):
    data = Wow_model.objects.get(id = id)
    data.delete()
    
    return redirect("/display/")

def displayEdit(request, id):
    data = Wow_model.objects.get(id = id)
    context = {"dataEdit": data}
    
    if request.method == 'POST':
        value = Wow_form(request.POST, request.FILES, instance = data)
        if value.is_valid():
            data.save()
            return redirect("/display/")
    
    return render(request, "edit.html", context)


# views begins        

class signup_view(View):
    def get(self, request):
        form = User_auth()
        return render(request, "register.html", {"form": form})
    
    def post(self, request):
        form = User_auth(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request, "account created successfully")
            return redirect(reverse("signin"))
        else:
            messages.success(request, "failed to create account")
            return render(request, "register.html", {"form": form})
        
class login_view(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")  
            pwd = form.cleaned_data.get("password")
            usr = authenticate(request, username=uname, password=pwd)
            if usr:
                login(request, usr)
                return redirect(reverse("home"))
            else:
                messages.error(request, "Invalid username or password")
                return render(request, "login.html", {"form":form})
        else:
            messages.error(request, "Form is not valid")
            return render(request, "login.html", {"form": form})

class LogoutView(View):
    
    def post(self, request):
        logout(request)
        return redirect(reverse("home"))