from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm
from .models import Task

class SuccessView(TemplateView):
    template_name = "success.html"

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "register.html"
    # redirect_authenticated_user = True
    success_url = reverse_lazy("login") 
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class CustomLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")

    def get_success_url(self):
        return self.success_url
    
class IndexView(TemplateView):
    template_name = "index.html"
  
###########################################  
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasklistview.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context
    
class TaskDetailView(ListView):
    pass
    
    
    