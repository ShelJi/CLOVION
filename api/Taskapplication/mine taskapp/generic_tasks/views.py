#  this code doesnt work mainly because of template_name in edit delete

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, FormView, UpdateView, DeleteView
from django.views import View
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from api.models import *
from .forms import *

class HomeView(LoginRequiredMixin, ListView):
    model = TaskModel
    template_name = "index.html"
    context_object_name = "datas"
    login_url = '/generic_tasks/login/'
    
    def get_queryset(self):
        return TaskModel.objects.filter(task_user_id=self.request.user.id)
    
class q_LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, "User does not exists")
            return super().form_invalid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, "Invalid Data")
        return super().form_invalid(form)
    
class CustomLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy("login")
    
class CustomLoginView(LoginView):
    template_name = "customloginform.html"
    # success_url redirects to default link which is details/profile/
    # success_url = reverse_lazy("home")
    
    def get_success_url(self):
        # next = self.request.GET.get("next")
        # if next:
        #     return next
        return reverse_lazy("home")
    
class SignupView(CreateView):
    template_name = "signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("home")
    
class TaskView(LoginRequiredMixin, CreateView):
    form_class = TaskForm
    # template_name = reverse_lazy("home")
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        formupdate = form.save(commit=False)
        formupdate.task_user = self.request.user
        formupdate.save()
        messages.success(self.request, "Task created succesfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Invalid data")
        return super().form_invalid(form)
    
class EditView(LoginRequiredMixin, UpdateView):
    model = TaskModel
    fields = []
    template_name = reverse_lazy("home")
    success_url = reverse_lazy("home")
    
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.task_status = not task.task_status
        task.save()
        return redirect(self.success_url)

# class EditView(View):
    def post(self, request, id, *args, **kwargs):
        task = get_object_or_404(TaskModel, id=id)
        
        # Toggle the task_status field
        task.task_status = not task.task_status
        task.save()
        
        return redirect(reverse_lazy('home'))

class DelView(LoginRequiredMixin, DeleteView):
    model = TaskModel
    # template_name = "task confirm del.html"
    success_url = reverse_lazy("home")