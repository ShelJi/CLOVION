from django.urls import path
from api import views

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()

# router.register("accounts/users",views.UsersView,basename="users")

urlpatterns = [
    # path("index/", views.IndexAPI.as_view(), name="home"),
    # path("signup/", views.SignupAPI.as_view(), name="signup"),
    # path("login/", views.LoginAPI.as_view(), name="login"),
    # path("logout/", views.LogoutAPI.as_view(), name="logout"),
    # path("task/", views.taskview, name="task"),
    # path("edit/<int:id>/", views.editview, name="edit"),
    # path("delete/<int:id>/", views.delview, name="delete"),
    
    # path("token/", TokenObtainPairView.as_view()),
    # path("token/refresh/", TokenRefreshView.as_view()),

]+ router.urls