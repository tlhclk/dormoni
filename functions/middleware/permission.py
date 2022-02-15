# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
from django.shortcuts import get_object_or_404
import logging

request_logger = logging.getLogger('django')


class PermissionMiddleware(MiddlewareMixin):
	def process_request(self, request):pass


	
	def process_response(self, request, response):
		ip = request.META["REMOTE_ADDR"]
		path = request.META["PATH_INFO"].split("?")[0].strip()
		return response