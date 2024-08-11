from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("index/", views.index, name="index"),
    path("details/", views.details, name="details"),
    path("", views.redirect_to, name="redirect"),
]
