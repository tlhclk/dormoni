# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
from django.shortcuts import get_object_or_404


class PermissionMiddleware(MiddlewareMixin):
	def process_request(self, request):pass
		


	
	def process_response(self, request, response):
		path = request.path
		global_valid_pages_list=['/404', '/500', '/400', '/300', '/', '/authentication/register/', '/authentication/login/', '/authentication/register_validation/',
		 '/authentication/password_reset/', '/authentication/password_reset/done/', '/authentication/password_change/', '/authentication/password_change/done/',
		 '/authentication/reset/done/', '/authentication/logout/', '']
		if request.is_ajax():
			if request.user.is_anonymous:
				if path in global_valid_pages_list or 'static' in path or 'media' in path:
					return response
				return redirect('/')
		else:
			if request.user.is_anonymous:
				if path in global_valid_pages_list or 'static' in path or 'media' in path:
					return response
				else:
					return redirect('/authentication/login/')
			else:
				return response