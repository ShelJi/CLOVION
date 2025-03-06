from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('empty_get_print/', views.empty_get_print, name="empty_get_print"),
    path('empty_get_print_many/', views.empty_get_print_many, name="empty_get_print_many"),
    path('empty_get_print_simple/', views.empty_get_print_simple, name="empty_get_print_simple"),
    path('empty_get_print_simple_many/', views.empty_get_print_simple_many, name="empty_get_print_simple"),
    
    path('empty_post/', views.empty_post, name="empty_post"),
    
    path('task_post/', views.task_post, name="task_post"),
    
    path('all_data_view/', views.all_data_view, name="all_data_view"), 
    path('task_user/', views.task_user, name="task_user"),
]
