from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('edit/<id>', views.EditView.as_view(), name='edit'),
    path('<id>/delete/', views.DeleteView.as_view(), name='delete'),
]
