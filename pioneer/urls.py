from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include 
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts import views as user_views

# #from . import views as core_views
# #from django.views.generic.base import TemplateView

# #from rest_framework.authtoken import views
#from blog.views import *
# from accounts.views import *



urlpatterns = [
   path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
   path('accounts/', include('accounts.urls')),
   path('blog/', include('blog.urls', namespace='blog')),
   path ('courses/', include('courses.urls')),
   path('', views.index, name='index'),
   path('special/',views.special, name='special'),
   path('logout/', views.user_logout, name='logout'),
    
   path('accounts/login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), #login url

   path('accounts/password-reset/', auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html'),
            name='password_reset'),
    
   path('accounts/password-reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
         ), name='password_reset_done'),
    
   path('accounts/password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'
         ), name='password_reset_confirm'),
    
   path('accounts/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
         ), name='password_reset_complete'),
    
    

]
if settings.DEBUG: 

        urlpatterns += static(settings.MEDIA_URL, 

                              document_root=settings.MEDIA_ROOT) 
 

