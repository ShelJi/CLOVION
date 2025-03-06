from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'viewsetzz', views.IndexViewsets, basename='viewsetzz')
# urlpatterns = router.urls

urlpatterns = [
    path('hello/', include(router.urls)),
    
    # function based
    path('index/', views.index),
    path('person/', views.person),
    path('personSimple/',views.personSimple),
    path('personForeign/',views.personForeign),
    
    # class based 
    path('IndexView/', views.IndexView.as_view()),

]