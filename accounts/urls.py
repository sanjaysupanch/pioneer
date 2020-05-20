from django.urls import path, include
from .import views 
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from accounts import views as user_views

app_name = "accounts"


urlpatterns = [
    path('register/', views.register, name='register'),
    #path('login/', views.user_login, name='user_login'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/password/',views.change_password,name='change_password'),
    path('change-password/', views.change_password, name='change_password'),
    url(r'^profile/(?P<pk>\d+)/$',views.view_profile,name='view_profile_with_pk'),
    
    
    
    
    # path('password-reset/', 
    #     auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'
    #     ),name='password_reset'), # password reset url
    #     #password reset done url
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
    #     name='password_reset_done'),
    #     #password reset confirm url
    # path('password-reset-confirm/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
    #     name='password_reset_confirm'),
    #     #password reset complete url
    # path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'), 
    #     name='password_reset_complete'),
    #     #path('reset/real', include('django.contrib.auth.urls')),

    

]