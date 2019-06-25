from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views
#from django.conf.urls import url



urlpatterns = [
    path('home/', views.index, name='index'),
]