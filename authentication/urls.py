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
    
    #path('new_user/', (views.NewUserView.as_view()), name='NewUserPage'),
    path('list/AuthenticationUser',views.ListAuthenticationUser.as_view(),name="List_AuthenticationUser"),
    path('list/AuthenticationGroup',views.ListAuthenticationGroup.as_view(),name="List_AuthenticationGroup"),
    path('list/Branch',views.ListBranch.as_view(),name="List_Branch"),
    path('list/Company',views.ListCompany.as_view(),name="List_Company"),
    path('create/AuthenticationUser',views.CreateAuthenticationUser.as_view(),name="Create_AuthenticationUser"),
    path('create/AuthenticationGroup',views.CreateAuthenticationGroup.as_view(),name="Create_AuthenticationGroup"),
    path('create/Branch',views.ListBranch.as_view(),name="Create_Branch"),
    path('create/Company',views.ListCompany.as_view(),name="Create_Company"),
 ]