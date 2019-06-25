from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('register/', views.registration, name='registration'),
]