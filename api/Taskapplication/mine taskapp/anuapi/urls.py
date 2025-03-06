from django.urls import path
from anuapi import views

urlpatterns = [
    path('studentcreate',views.studentcreate),
    path('studentdisplay',views.studentdisplay),
]