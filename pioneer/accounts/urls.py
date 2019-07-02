from django.urls import path, include
from .import views 
from django.contrib.auth import views as auth_views
from django.conf.urls import url
app_name = "accounts"


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/password/',views.change_password,name='change_password'),
    path('change-password/', views.change_password, name='change_password'),
    path('reset-password/',auth_views.PasswordResetView.as_view(template_name='accounts/reset_password.html'
        ,email_template_name = 'accounts/reset_password_email.html'),name='password_reset'), # password reset url
        # password reset done url
    path('reset-password/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'),
        name='password_reset_done'),
        #password reset confirm url
    path('reset-password/confirm/(<uidb64>[0-9A-Za-z]+)-(<token>.+)/',
        auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset_password_confirm.html'),
        name='password_reset_confirm'),
        #password reset complete url
    path('reset-password/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'),name='password_reset_complete'),
        #path('reset/real', include('django.contrib.auth.urls')),

    url(r'^profile/(?P<pk>\d+)/$',views.view_profile,name='view_profile_with_pk'),


]