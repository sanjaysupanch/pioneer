from django.urls import path, include
from .import views 
from django.conf.urls import url

app_name = "blog"


urlpatterns = [
    path('add/', views.add_blog, name='add_blog'),
    path('', views.show, name="show"),
    path('<slug:slug>/', views.view_post, name='post_detail'),
    #path('sana/', views.ps, name="PostList")
    
]