# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
from django.shortcuts import get_object_or_404
from schema.models import PathModel
from django.urls import resolve


class PermissionMiddleware(MiddlewareMixin):
	def process_request(self, request):pass
		


	
	def process_response(self, request, response):
		path = request.path
		url_name=resolve(path).url_name
		path_queryset = PathModel.objects.filter(name=url_name)

		if request.user.is_superuser:
			return response
		elif request.user.is_anonymous:
			if path_queryset[0].code.startswith("00") or 'static' in path or 'media' in path:
				return response
			else:
				return redirect('/authentication/login/')
		else:
			if len(path_queryset)>0:
				return response
			else:
				return redirect('/')
