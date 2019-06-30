from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from accounts import views
#from base import views

# from django.contrib import admin
# from django.conf.urls import include, url
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

# from django.contrib.auth import views as auth_views
# #from . import views as core_views
# #from django.views.generic.base import TemplateView

# #from rest_framework.authtoken import views
# from base.views import *
# from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('base/', include('base.urls')),
    path('accounts/', include('accounts.urls')),
    path('', views.index, name='index'),
    path('special/',views.special, name='special'),
    path('logout/', views.user_logout, name='logout'),

]