from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

# generic_tasks_good
urlpatterns = [
    path("success/", views.SuccessView.as_view(), name='success'),
    
    path("register/", views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),

    path('', views.IndexView.as_view(), name="index"),
    path('tasks/', views.TaskListView.as_view(), name="tasks"),
    path('task_detail/<int:pk>/', views.TaskDetailView.as_view(), name='task'),
]
