from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('sellerLogin/', views.sellerLogin, name='seller'),
    path('newseller/', views.newseller, name='newseller'),
    path('seller/<int:id>/', views.seller, name='sellerpage'),
    path('sellerProfile/<int:id>/', views.profile, name='sellerProfile'),
    path('edit/<int:id>/', views.edit, name='selleredit'),
    path('delete/<int:id>/', views.delete, name='productDelete'),
    path('userProfile/', views.userProfile, name='userProfile'),
    
    path('<str:empty>/', views.emptyRedirect, name= 'reverse'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
