from django.urls import path
from generic_tasks import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.q_LoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("custom-login/", views.CustomLoginView.as_view(), name="custom_login"),
    path("task/", views.TaskView.as_view(), name="task"),
    path("edit/<int:pk>/", views.EditView.as_view(), name="edit"),
    path("delete/<int:pk>/", views.DelView.as_view(), name="delete"),
]
