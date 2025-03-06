from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'task_list' # this will contrls th redirect of files in another app url with same name

urlpatterns = [
    path("all-data/", views.AllDatasView.as_view(), name="all-data"),
    path("task-user/", views.UserTaskView.as_view(), name="task-user"),
    path("task/<int:pk>/", views.TaskView.as_view(), name="task"),
    path("task-edit/<int:pk>/", views.TaskEditView.as_view(), name="task-edit"),
    path("task-del/<int:pk>/", views.TaskDelView.as_view(), name="task-del"),
    path("task-create/", views.TaskCreateView.as_view(), name="task-create"),
    
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('register/', views.RegisterView.as_view(), name="register"),
]
    