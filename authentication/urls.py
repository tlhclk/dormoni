# -*- coding: utf-8 -*-
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'authentication'
urlpatterns = [
 path('register/', (views.MyRegisterView.as_view()), name='RegisterPage'),
 path('login/', (views.MyLoginView.as_view()), name='LoginPage'),
 path('logout/', (views.MyLogOutView.as_view()), name='LogoutPage'),
 path('password_change/done', (auth_views.PasswordChangeDoneView.as_view()), name='password_change_done'),
 path('password_change', (auth_views.PasswordChangeView.as_view()), name='change-password'),
 path('reset/done', (auth_views.PasswordResetCompleteView.as_view()), name='password_reset_complete'),
 path('reset/<uidb64>/<token>', (auth_views.PasswordResetConfirmView.as_view()), name='password_reset_confirm'),
 path('password_reset/done', (auth_views.PasswordResetDoneView.as_view()), name='password_reset_done'),
 path('password_reset/', (auth_views.PasswordResetView.as_view()), name='password_reset'),
 path('ip_validation/', (views.IpValidationView.as_view()), name='ip_validation')]