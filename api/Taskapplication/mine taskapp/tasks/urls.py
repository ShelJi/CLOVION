from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.homeview, name="home"),
    path("signup/", views.signupview, name="signup"),
    path("login/", views.loginview, name="login"),
    path("logout/", views.logoutview, name="logout"),
    path("task/", views.taskview, name="task"),
    path("edit/<int:id>/", views.editview, name="edit"),
    path("delete/<int:id>/", views.delview, name="delete"),
]
