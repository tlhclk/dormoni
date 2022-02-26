# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'function'
urlpatterns = [
    path('to_export/', views.ToExportView.as_view(), name='ToExportPage'),
 ]
 