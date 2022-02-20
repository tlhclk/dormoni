# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
 path('', (views.IndexPage.as_view()), name='IndexPage'),
 path('home/', (views.HomePage.as_view()), name='HomePage'),
 path('admin/', admin.site.urls),
 path('authentication/', include('authentication.urls')),
 path('parameters/', include('parameters.urls')),
 path('people/', include('people.urls'))
  ] + static((settings.MEDIA_URL), document_root=(settings.MEDIA_ROOT)) + static((settings.STATIC_URL), document_root=(settings.STATIC_ROOT))

def handler404(request, exeption):
    return render(request, 'error_page.html')


def handler403(request, exception):
    return render(request, 'error_page.html')


def handler400(request, exception):
    return render(request, 'error_page.html')


def handler500(request):
    return render(request, 'error_page.html')