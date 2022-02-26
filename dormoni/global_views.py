# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.http import request
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from functions.template.custom_view import CustomListView
from functions.TableFuncs import ObjectFunc
from functions.QuerySetFuncs import ModelQueryset
from authentication.models import OperationHistoryModel
from parameters.models import OperationTypeModel

class GlobalListView(ListView):
    template_name = 'global_list.html'
    paginate_by = 50
    action = 'List'
    fields = []

    def get_extras(self):
        extra_dict = {}
        for item in self.request.GET:
            extra_dict[item] = self.request.GET[item]
        return extra_dict

    def get_queryset(self):
        mq = ModelQueryset(self.request, self.kwargs['table_name'], self.action)
        object_list = mq.get_queryset()
        self.field_list = mq.get_table_field_list(mq.table_obj, self.action)
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        mq = ModelQueryset(self.request, self.kwargs['table_name'], self.action)
        context = super(GlobalListView, self).get_context_data()
        context['table_name'] = mq.table_obj.name
        context['title'] = mq.table_obj.list_title
        context['fields'] = self.field_list
        return context