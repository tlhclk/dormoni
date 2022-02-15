# -*- coding: utf-8 -*-
from django.urls import path
from . import views
app_name = 'functions'
urlpatterns = [
 path('GetNotifications/', (views.GetNotifications.as_view({'get': 'list'})), name='GetNotifications'),
 path('GetReportData/', (views.get_report_data), name='GetReportData')]