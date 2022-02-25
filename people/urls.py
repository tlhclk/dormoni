# -*- coding: utf-8 -*-
from django.urls import path
from . import views
app_name = 'people'
urlpatterns = [
    path('list/Person',views.ListPerson.as_view(),name="List_Person")
    ]