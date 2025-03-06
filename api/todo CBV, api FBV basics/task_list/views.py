from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models

class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("task_list:login")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
  
class LoginView(LoginView):
    # this will not work if the same named file present in anoher app, specifying Template_name will solve this
    redirect_authenticated_user = True
    success_url = reverse_lazy("task_list:task-user")
    
    def get_success_url(self) -> str:
        return self.success_url
    
# path for template <appname>/<modelname>_list.html
# default context name - object_list 
# this default value still work even context_object_name is set
class AllDatasView(ListView):
    model = models.Task
    context_object_name = 'tasks'
    
class UserTaskView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("task_list:login")
    model = models.Task
    context_object_name = 'tasks'
    # template_name = ""
     
    def get_queryset(self):
        return models.Task.objects.filter(user = self.request.user)

# path for template <appname>/<modelname>_detail.html
# default context name - object
class TaskView(DetailView):
    model = models.Task

# path for template <appname>/<modelname>_form.html
class TaskEditView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("task_list:login")
    model = models.Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy("task_list:task-user")
    
class TaskDelView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("task_list:login")
    model = models.Task
    success_url = reverse_lazy("task_list:task-user")
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("task_list:login")
    model = models.Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("task_list:task-user")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
  