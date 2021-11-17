# -*- coding: utf-8 -*-
### import_part
from django.urls import path
from . import views

### pattern_part
app_name='functions'
urlpatterns= [
	path('GetNotifications/',views.GetNotifications.as_view({'get': 'list'}),name="GetNotifications"),

]