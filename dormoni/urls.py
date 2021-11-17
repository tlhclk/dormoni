# -*- coding: utf-8 -*-
### import_part
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from . import views,global_views


### path_part
urlpatterns = [
	path('',views.IndexPage.as_view(),name="IndexPage"),
	path('home/',views.HomePage.as_view(),name="HomePage"),
	path('toexport/',views.ToexportPage.as_view(),name="ToexportPage"),

	# Global Pages
	path('global_create/<str:table_name>/',global_views.GlobalCreateView.as_view(),name='global_create'),
	path('global_delete/<str:table_name>/<int:pk>/',global_views.GlobalDeleteView.as_view(),name='global_delete'),
	path('global_detail/<str:table_name>/<int:pk>/',global_views.GlobalDetailView.as_view(),name='global_detail'),
	path('global_list/<str:table_name>/',global_views.GlobalListView.as_view(),name='global_list'),
	path('global_update/<str:table_name>/<int:pk>/',global_views.GlobalUpdateView.as_view(),name='global_update'),
	
	# İncludes
	path('admin/',admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)

def handler404(request,exeption):
	return render(request,"error_page.html")
def handler403(request,exception):
	return render(request,"error_page.html")
def handler400(request,exception):
	return render(request,"error_page.html")
def handler500(request):
	return render(request,"error_page.html")