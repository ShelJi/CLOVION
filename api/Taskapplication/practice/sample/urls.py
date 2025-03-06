from django.urls import path, include
from sample import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.NewViewset, basename='user')

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('new/', views.NewViews.as_view(), name='new'),
    path('', include(router.urls))
]

