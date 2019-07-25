from django.urls import path, include
from .import views
from django.conf.urls import url

app_name = "courses"


urlpatterns = [
    path('', views.course, name='view_course'),
    path('b-to-adv/', views.b_to_adv, name="basic"),
    path('speaking/', views.speaking, name="speaking"),
    path('expository/', views.expository, name="expository"),
    path('vocabulary/', views.vocabulary, name="vocabulary"),
    path('c_segment/', views.c_segment, name="c_segment"),
    path('grammar/', views.grammar, name="grammar"),
    path('about-us/', views.about_us, name="about_us"),
    
]