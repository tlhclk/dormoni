# -*- coding: utf-8 -*-
from django.shortcuts import redirect
import logging
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
from django.shortcuts import get_object_or_404
from authentication.models import HistoryLogModel, UserIpModel
from .TableFuncs import ObjectFunc
request_logger = logging.getLogger('django')

class LoggerMiddleware(MiddlewareMixin, ObjectFunc):

    def process_request(self, request):
        if 'sessionid' in request.COOKIES:
            session = request.COOKIES['sessionid']
        else:
            session = None
        if 'csrftoken' in request.COOKIES:
            csrftoken = request.COOKIES['csrftoken']
        else:
            csrftoken = None
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        ip_address = request.META.get('REMOTE_ADDR')
        path = request.META['PATH_INFO']
        if 'static' not in path:
            if 'media' not in path:
                method = request.method
                date = datetime.now()
                time = datetime.now()
                model = HistoryLogModel
                last_record = model.objects.create(date=date, time=time, ip_address=ip_address, hyperlink=path, action=method, user_id=user, session=session, csrf_token=csrftoken)
                message = last_record.logger_str()
                auth = self.ip_check(ip_address)
                if auth:
                    request_logger.info(message)
                else:
                    request_logger.info(message + ' ://unauthorized_ip')

    def ip_check(self, ip_address):
        obj = get_object_or_404(UserIpModel, ip_address=ip_address)
        if obj.permission:
            return True
        return False

    def process_response(self, request, response):
        ip = request.META['REMOTE_ADDR']
        path = request.META['PATH_INFO'].split('?')[0].strip()
        valid_pages = ['/404', '/500', '/400', '/300', '/', '/authentication/register/', '/authentication/login/', '/authentication/register_validation/',
         '/authentication/password_reset/', '/authentication/password_reset/done/', '/authentication/password_change/', '/authentication/password_change/done/',
         '/authentication/reset/done/', '/authentication/logout/', '']
        if request.is_ajax():
            return response
            if request.user.is_anonymous:
                if path in valid_pages or 'static' in path or 'media' in path:
                    return response
                return redirect('/')
        else:
            if path in valid_pages or 'static' in path or 'media' in path:
                return response
            auth = self.ip_check(ip)
            if auth == True:
                return response
            return redirect('/?warning=unauthorized_ip')