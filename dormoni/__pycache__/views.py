# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\myerp\views.py
# Compiled at: 2021-12-30 14:55:28
# Size of source mod 2**32: 3247 bytes
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from functions.TableFuncs import ObjectFunc
from functions.GlobalFunc import StandardListPagination
from authentication.models import OperationHistoryModel
from parameters.models import OperationTypeModel

class IndexPage(View):
    template_name = 'base.html'

    def get_context_data(self):
        context_data = {}
        context_data['title'] = 'Hoş Geldiniz'
        return context_data

    def get(self, request):
        return render(request, (self.template_name), context=(self.get_context_data()))


class HomePage(View):
    template_name = 'home.html'

    def get_context_data(self):
        context_data = {}
        context_data['title'] = 'Ana Sayfa'
        return context_data

    def get(self, request):
        return render(request, (self.template_name), context=(self.get_context_data()))


class GlobalTableView(viewsets.ModelViewSet):
    filter_backends = [
     DjangoFilterBackend]
    filter_fields = '__all__'
    pagination_class = StandardListPagination

    def get_queryset(self):
        of = ObjectFunc()
        table_name = self.kwargs.get('table_name')
        table_model = of.get_table_model(table_name)
        return table_model.objects.all()

    def get_serializer_class(self):
        of = ObjectFunc()
        table_name = self.kwargs.get('table_name')
        table_obj = of.get_table_obj(table_name)
        exec('from %s.serializers import %sSerializer' % (table_obj.app_id.name, table_obj.name[:-5]))
        serializer_class = eval(table_obj.name[:-5] + 'Serializer')
        return serializer_class

    def initialize_request(self, request, *args, **kwargs):
        return (super().initialize_request)(request, *args, **kwargs)

    @action(detail=True, methods=['POST', 'PUT', 'PATCH', 'DELETE'])
    def create_log(self):
        table_name = self.kwargs.get('table_name')
        of = ObjectFunc()
        table_obj = of.get_table_obj(table_name)
        table_model = of.get_table_model(table_name)
        primary_key = self.kwargs.get('pk')
        if primary_key:
            object = get_object_or_404(table_model, pk=primary_key)
        else:
            object = None
        method = get_object_or_404(OperationTypeModel, code=(self.request.method.lower()))
        if method.id in (2, 3, 4):
            detail = self.get_form_detail(obj=object)
        else:
            if method.id == 1:
                detail = self.get_form_detail(self.request.POST, 'POST')
            else:
                detail = 'fields:[], values:[]'
        dt = datetime.now()
        user_id = self.request.user
        oh_obj = OperationHistoryModel.objects.create(table_id=table_obj, primary_key=primary_key, type_id=method, detail=detail, datetime=dt, user_id=user_id)
        oh_obj.save()

    def get_form_detail(self, post_data=None, obj=None):
        field_list = []
        value_list = []
        if post_data:
            for key, value in post_data.items():
                if key != 'csrfmiddlewaretoken':
                    field_list.append(key)
                    value_list.append(str(value))

        else:
            if obj:
                for field in obj._meta.get_fields():
                    if hasattr(field, 'column') and field.name != 'id':
                        field_list.append(field.name)
                        value_list.append(getattr(obj, field.name))

            else:
                return 'fields:[], values:[]'
        return 'fields:[%s], values:[%s]' % (', '.join(field_list), ', '.join(value_list))