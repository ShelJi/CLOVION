from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('api/tasks',views.TaskViewSet,basename="tasks")
router.register('api/v1/tasks',views.TaskmodelViewsetView,basename="modeltasks")
router.register("users",views.UsersView,basename="users")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/',views.TaskView.as_view()),
    path('tasks/<int:id>/',views.TaskDetailView.as_view()),
    path('',include("taskweb.urls"))
]+router.urls
