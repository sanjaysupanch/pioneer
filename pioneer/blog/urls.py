from django.urls import path, include
from .import views 
from django.conf.urls import url

app_name = "blog"


urlpatterns = [
    path('', views.add_blog, name='add_blog'),
    path('<slug:slug>/', views.view_post, name='view_post'),
    #path('sana/', views.ps, name="PostList")
    
]