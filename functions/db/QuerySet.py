# -*- coding: utf-8 -*-
import django.apps as apps
from django.db.models import Q
from .TableFuncs import ObjectFunc
import datetime

class ModelQueryset(ObjectFunc):

    def __init__(self, request, table_name, action, fd={}, ed={}, *args, **kwargs):
        self.request = request
        self.user = request.user
        self.url_name = request.resolver_match.url_name
        self.action = action
        self.fd = fd
        self.ed = ed
        self.search_text = ''
        self.extra_dict = self.get_extra_dict()
        self.request_kwargs = request.resolver_match.kwargs
        self.kwargs = kwargs
        self.table_name = table_name
        self.table_obj = self.get_table_obj(self.table_name)
        self.table_model = self.get_table_model(self.table_obj)

    def get_extra_dict(self):
        extra_dict = {}
        for key in self.request.GET:
            if key != 'page':
                if key == 'search':
                    self.search_text = self.request.GET[key]
                else:
                    extra_dict[key] = self.request.GET[key]
        return extra_dict

    def get_field_data(self, ftype, f1, value, f2=None):
        key_str = None
        value_str = None
        if f2:
            f1 = '%s__%s' % (f1, f2)
        if ftype == 'CharField' or ftype == 'EmailField':
            key_str = '%s__%s' % (f1, 'icontains')
            value_str = value
        elif ftype == 'BooleanField':
            key_str = '%s' % f1
            if value.lower() == 'true' or value == '1':
                value_str = True
            elif value.lower() == 'false' or value == '0':
                value_str = False
        elif ftype == 'DateField':
            key_str = '%s' % f1
            ymd_list = value.split('-')
            try:
                year, month, day = ymd_list
                date = datetime.date(int(year), int(month), int(day))
                value_str = date
            except ValueError:
                pass
        elif ftype == 'TimeField':
            key_str = '%s' % f1
            hm_list = value.split(':')
            try:
                hour, minutes = hm_list
                time = datetime.time(int(hour), int(minutes))
                value_str = time
            except ValueError:
                pass
        elif ftype == 'id':
            key_str = '%s_id' % f1
            value_str = int(value)
        return (key_str, value_str)

    def get_search_filter_data(self):
        sfor = Q()
        for field in self.get_table_field_list(self.table_obj, self.action):
            if field.field == 'ForeignKey':
                field_list2 = self.get_table_field_list(field.to, 'All')
                for field2 in field_list2:
                    key, value = self.get_field_data(field2.field, field.name, self.search_text, field2.name)
                    if key != None and value != None:
                        sfor |= Q((key, value))

            else:
                key, value = self.get_field_data(field.field, field.name, self.search_text)
                if key != None and value != None:
                    sfor |= Q((key, value))
        return sfor

    def get_field_filter_data(self):
        ffand = Q()
        for field in self.get_table_field_list(self.table_obj, self.action):
            if field.field=="ForeignKey":
                if field.name in self.extra_dict:
                    field_list2 = self.get_table_field_list(field.to, 'All')
                    for field2 in field_list2:
                        key, value = self.get_field_data(field2.field, field.name, self.extra_dict[field.name], field2.name)
                        if key != None and value != None:
                            ffand |= Q((key, value))
                elif '%s_id' % field.name in self.extra_dict:
                    ffand &= Q(('%s_id' % field.name, self.extra_dict[('%s_id' % field.name)]))
            else:
                if field.name in self.extra_dict:
                    key, value = self.get_field_data(field.field, field.name, self.extra_dict[field.name])
                    if key != None and value != None:
                        ffand &= Q((key, value))
        return ffand

    def get_exclude_data(self):
        edor = Q()
        for key, value in self.ed.items():
            edor |= Q((key, value))
        return edor

    def get_queryset(self):
        object_list = self.table_model.objects.all()
        for key, value in self.fd.items():
            object_list = object_list.filter(Q((key, value)))
        if len(self.extra_dict) > 0:
            if self.search_text != '':
                ffand = self.get_field_filter_data()
                object_list = object_list.filter(ffand)
                sfor = self.get_search_filter_data()
                object_list = object_list.filter(sfor)
            else:
                ffand = self.get_field_filter_data()
                object_list = object_list.filter(ffand)
        else:
            if self.search_text != '':
                sfor = self.get_search_filter_data()
                object_list = object_list.filter(sfor)
        if len(self.ed) > 0:
            edor = self.get_exclude_data()
            object_list = object_list.exclude(edor)
        return object_list