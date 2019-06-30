import django.urls
from django.urls import path, include
from .import views 
from django.contrib.auth import views as auth_views
from django.conf.urls import url
app_name = "accounts"


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/', views.view_profile, name='profile'),


]