# -*- coding: utf-8 -*-

import django.apps as apps
from django.db.models import Q, Sum, Value, F, Func,Count
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField
from django.db.models.functions import ExtractMonth, ExtractWeek, ExtractYear, Concat, Coalesce, Right
from django.shortcuts import get_object_or_404
from .TableFuncs import AttrDict, ObjectFunc
from main.models import ReportModel, ReportFilterModel
import operator, datetime, json

datetime_fields = ['DateField', 'TimeField', 'DateTimeField']
value_fields = ['IntegerField', 'DecimalField', 'FloatField']

# class GetReportData:
#     def __init__(self, request):
#         self.of = ObjectFunc()
#         self.limit = -1
#         self.gf, self.tf, self.vf = (None, None, None)
#         self.order_by_list = []
#         self.sub_datetime = ''
#         self.extra_dict = {}
#         self.report_obj = None
#         for key in request.GET:
#             if 'report_code' == key:
#                 report_list = ReportModel.objects.filter(code=(request.GET.get(key)))
#                 if len(report_list) > 0:
#                     self.report_obj = report_list[0]
#                     self.table_model = self.of.get_table_model(self.report_obj.table_id)
#                 else:
#                     if key not in self.extra_dict:
#                         self.extra_dict[key] = [
#                          request.GET.get(key)]
#             else:
#                 self.extra_dict[key].append(request.GET.get(key))

#     def get_json_data(self):
#         json_dict = {'dataset': {}}
#         temp_list = []
#         for obj in self.get_data():
#             if self.report_obj.group_by_field_id:
#                 if self.report_obj.text_field_id:
#                     if self.report_obj.text_field_id.field not in datetime_fields:
#                         temp_list.append((obj[self.report_obj.group_by_field_id.name], obj[self.report_obj.text_field_id.name], obj['total_value']))
#                     else:
#                         temp_list.append((obj[self.report_obj.group_by_field_id.name], obj['partial_date'], obj['total_value']))
#                 else:
#                     temp_list.append((obj[self.report_obj.group_by_field_id.name], '-0-', obj['total_value']))
#             elif self.report_obj.text_field_id:
#                 if self.report_obj.text_field_id.field not in datetime_fields:
#                     temp_list.append(('-0-', obj[self.report_obj.text_field_id.name], obj['total_value']))
#                 else:
#                     temp_list.append(('-0-', obj['partial_date'], obj['total_value']))
#             else:
#                 temp_list.append(('-0-', '-0-', obj['total_value']))
#         else:
#             temp_list = self.get_ordered_query(temp_list)
#             for item in temp_list:
#                 if item[0] not in json_dict['dataset']:
#                     json_dict['dataset'][item[0]] = {'text_data':[
#                       item[1]], 
#                      'value_data':[item[2]]}
#                 else:
#                     json_dict['dataset'][item[0]]['text_data'].append(item[1])
#                     json_dict['dataset'][item[0]]['value_data'].append(item[2])
#             else:
#                 if self.limit == -1:
#                     max_list = []
#                     for gkey in json_dict['dataset']:
#                         sum_val = sum(json_dict['dataset'][gkey]['value_data'])
#                         max_list.append((gkey, sum_val))
#                     else:
#                         max_list = sorted(max_list, key=(lambda tup: tup[1]), reverse=True)
#                         max_list = max_list[5:]
#                         max_key, max_value = map(list, zip(*max_list))
#                         for gkey in max_key:
#                             if gkey in max_key:
#                                 del json_dict['dataset'][gkey]

#                 json_dict = self.get_titles(json_dict)
#         return json_dict

#     def get_data(self):
#         if self.report_obj:
#             object_list = self.get_master_queryset()
#             object_list = object_list.order_by()
#             if self.report_obj.group_by_field_id:
#                 if self.report_obj.text_field_id:
#                     if self.report_obj.text_field_id.field not in datetime_fields:
#                         object_list = object_list.values(self.report_obj.group_by_field_id.name, self.report_obj.text_field_id.name)
#                     else:
#                         object_list = object_list.values(self.report_obj.group_by_field_id.name)
#                         if self.sub_datetime == 'year':
#                             object_list = object_list.annotate(year=(ExtractYear(self.report_obj.text_field_id.name)))
#                             object_list = object_list.annotate(partial_date='year')
#                         elif self.sub_datetime == 'month':
#                             object_list = object_list.annotate(year=(ExtractYear(self.report_obj.text_field_id.name)))
#                             object_list = object_list.annotate(month=(ExtractMonth(self.report_obj.text_field_id.name)))
#                             object_list = object_list.annotate(partial_date=Concat((F('year')), (Value('-')), (Right(Concat(Value('0'), F('month')), 2)), output_field=(CharField())))
#                         elif self.sub_datetime == 'week':
#                             object_list = object_list.annotate(year=(ExtractYear(self.report_obj.text_field_id.name)))
#                             object_list = object_list.annotate(week=(ExtractWeek(self.report_obj.text_field_id.name)))
#                             object_list = object_list.annotate(partial_date=Concat((F('year')), (Value('-')), (Right(Concat(Value('0'), F('week')), 2)), output_field=(CharField())))
#                 else:
#                     return [{'error': 'group_by_field seçilmemiştir'}]
#             else:
#                 if self.report_obj.text_field_id:
#                     if self.report_obj.value_field_id:
#                         if self.report_obj.group_count == '0':
#                             object_list = object_list.values('id', self.report_obj.text_field_id.name)
#                         else:
#                             object_list = object_list.values(self.report_obj.text_field_id.name)
#                     else:
#                         return [{'error': 'value_field seçilmemiştir'}]
#                 else:
#                     return [{'error': 'text_field seçilmemiştir'}]
#             if self.report_obj.group_count == '1':
#                 object_list = object_list.annotate(total_value=(Sum(self.report_obj.value_field_id.name)))
#             else:
#                 object_list = object_list.annotate(total_value=(Sum(self.report_obj.value_field_id.name)))
#         else:
#             return []
#         return object_list

#     def get_master_queryset(self):
#         fd, ed = self.get_filters()
#         fdata, edata = self.get_filter_data(fd, ed)
#         ol = self.table_model.objects.filter(fdata).exclude(edata)
#         return ol

#     def get_ordered_query(self, ol):
#         for ord in self.order_by_list:
#             if ord[0] == '-':
#                 if self.report_obj.group_by_field_id:
#                     if self.report_obj.group_by_field_id.name == ord[1:]:
#                         ol = sorted(ol, key=(lambda tup: tup[0]), reverse=True)
#                 if self.report_obj.text_field_id:
#                     if self.report_obj.text_field_id.name == ord[1:]:
#                         ol = sorted(ol, key=(lambda tup: tup[1]), reverse=True)
#                 if self.report_obj.value_field_id and self.report_obj.value_field_id.name == ord[1:]:
#                     ol = sorted(ol, key=(lambda tup: tup[2]), reverse=True)
#             else:
#                 if self.report_obj.group_by_field_id:
#                     if self.report_obj.group_by_field_id.name == ord:
#                         ol = sorted(ol, key=(lambda tup: tup[0]))
#                     elif self.report_obj.text_field_id and self.report_obj.text_field_id.name == ord:
#                         ol = sorted(ol, key=(lambda tup: tup[1]))
#                     if self.report_obj.value_field_id:
#                         if self.report_obj.value_field_id.name == ord:
#                             ol = sorted(ol, key=(lambda tup: tup[2]))
#                         if self.limit != -1:
#                             ol = ol[:self.limit]
#         return ol

#     def get_titles(self, jd):
#         jd['title'] = ''
#         jd['report_title'] = self.report_obj.title
#         jd['group_to_table'] = getattr(self.report_obj.group_by_field_id, 'to') if hasattr(self.report_obj.group_by_field_id, 'to') else ''
#         jd['group_to_field'] = getattr(self.report_obj.group_by_field_id, 'name') if hasattr(self.report_obj.group_by_field_id, 'name') else ''
#         jd['text_to_table'] = getattr(self.report_obj.text_field_id, 'to') if hasattr(self.report_obj.text_field_id, 'to') else ''
#         jd['text_to_field'] = getattr(self.report_obj.text_field_id, 'name') if hasattr(self.report_obj.text_field_id, 'name') else ''
#         jd['text_title'] = getattr(self.report_obj.value_field_id, 'verbose_name') if hasattr(self.report_obj.value_field_id, 'verbose_name') else ''
#         jd['value_to_table'] = getattr(self.report_obj.value_field_id, 'to') if hasattr(self.report_obj.value_field_id, 'to') else ''
#         jd['value_to_field'] = getattr(self.report_obj.value_field_id, 'name') if hasattr(self.report_obj.value_field_id, 'name') else ''
#         jd['value_title'] = getattr(self.report_obj.value_field_id, 'verbose_name') if hasattr(self.report_obj.value_field_id, 'verbose_name') else ''
#         jd['report_type'] = self.report_obj.report_type
#         jd['report_code'] = self.report_obj.code
#         if jd['group_to_table'] != '' and jd['group_to_table'] != None:
#             gt_model = self.of.get_table_model(self.report_obj.group_by_field_id.to)
#         else:
#             gt_model = None
#         if jd['text_to_table'] != '' and jd['text_to_table'] != None:
#             tt_model = self.of.get_table_model(jd['text_to_table'])
#         else:
#             tt_model = None
#         for gkey in jd['dataset']:
#             if gt_model != None:
#                 gtitle = get_object_or_404(gt_model, pk=(int(gkey)))
#                 jd['dataset'][gkey]['title'] = str(gtitle)
#             jd['dataset'][gkey]['text_title'] = jd['dataset'][gkey]['text_data']
#         for gkey in jd['dataset']:
#             if tt_model != None:
#                 jd['dataset'][gkey]['text_title'] = []
#                 for tkey in jd['dataset'][gkey]['text_data']:
#                     ttitle = get_object_or_404(tt_model, pk=(int(tkey)))
#                     jd['dataset'][gkey]['text_title'].append(str(ttitle))
#         return jd

#     def get_filters(self):
#         filter_list = ReportFilterModel.objects.filter(report_id=(self.report_obj))
#         filter_dict = {'1':[],  '3':[],  '4':[],  '5':[],  '6':[],  '7':[],  '10':[],  '11':[]}
#         exclude_dict = {'2':[],  '8':[]}
#         for filter in filter_list:
#             if filter.filter_type == '9':
#                 self.limit = int(filter.value)
#             if filter.field_id:
#                 if filter.field_id.field == 'ForeignKey':
#                     field_name = filter.field_id.name + '_id'
#                 else:
#                     field_name = filter.field_id.name
#         if filter.filter_type == '1':
#             filter_dict[filter.filter_type].append(Q((field_name, filter.value)))
#         elif filter.filter_type == '2':
#             exclude_dict[filter.filter_type].append(Q((field_name, filter.value)))
#         elif filter.filter_type == '3':
#             filter_dict[filter.filter_type].append(Q((field_name + '__gt', filter.value)))
#         elif filter.filter_type == '4':
#             filter_dict[filter.filter_type].append(Q((field_name + '__gte', filter.value)))
#         elif filter.filter_type == '5':
#             filter_dict[filter.filter_type].append(Q((field_name + '__lt', filter.value)))
#         elif filter.filter_type == '6':
#             filter_dict[filter.filter_type].append(Q((field_name + '__lte', filter.value)))
#         elif filter.filter_type == '7':
#             filter_dict[filter.filter_type].append(Q((field_name, filter.value)))
#         elif filter.filter_type == '8':
#             exclude_dict[filter.filter_type].append(Q((field_name, filter.value)))
#         elif filter.filter_type == '12':
#             self.order_by_list.append(filter.value + filter.field_id.name)
#         if not filter.filter_type == '':
#             if filter.filter_type == None:
#                 self.sub_datetime = filter.date_detail
#                 if filter.field_id.field in datetime_fields:
#                     if filter.filter_type == '10':
#                         cur_date = datetime.datetime.today()
#                         filter_dict[filter.filter_type].append(Q((field_name + '__gte', cur_date - self.get_date_filter_value(filter))))
#                     elif filter.filter_type == '11':
#                         cur_date = datetime.datetime.today()
#                         filter_dict[filter.filter_type].append(Q((field_name + '__lte', cur_date + self.get_date_filter_value(filter))))
#         return (filter_dict, exclude_dict)

#     def get_filter_data(self, fd, ed):
#         fdata = Q()
#         edata = Q()
#         for q_data in fd['1']:
#             fdata &= q_data
#         for q_data in ed['2']:
#             edata |= q_data
#         for q_data in fd['3']:
#             fdata &= q_data
#         for q_data in fd['4']:
#             fdata &= q_data
#         for q_data in fd['5']:
#             fdata &= q_data
#         for q_data in fd['6']:
#             fdata &= q_data
#         for q_data in fd['7']:
#             fdata |= q_data
#         for q_data in ed['8']:
#             edata &= q_data
#         for q_data in fd['10']:
#             fdata &= q_data
#         for q_data in fd['11']:
#             fdata &= q_data
#         return (fdata, edata)

#     def get_date_filter_value(self, filter):
#         if filter.date_detail == 'month':
#             multiplier = 30
#         else:
#             if filter.date_detail == 'year':
#                 multiplier = 365
#             elif filter.date_detail == 'week':
#                 multiplier = 7
#             else:
#                 multiplier = 1
#         return datetime.timedelta(days=(int(filter.value) * multiplier))

class GetReportData:
    def __init__(self,request):
        self.of = ObjectFunc()
        self.report_obj = None
        self.table_model=None
        self.extra_dict={}
        self.request=request
        self.get_request_data()

    def get_request_data(self):
        for key in self.request.GET:
            if 'report_code' == key:
                report_list = ReportModel.objects.filter(code=self.request.GET.get(key))
                if len(report_list) > 0:
                    self.report_obj = report_list[0]
                    self.table_model = self.of.get_table_model(self.report_obj.table_id)
                else:
                    if key not in self.extra_dict:
                        self.extra_dict[key] = [self.request.GET.get(key)]
            else:
                self.extra_dict[key].append(self.request.GET.get(key))

    def get_json_data(self):
        if self.report_obj:
            if self.report_obj.report_type=="1":
                pc = PieChart(self)
                return pc.get_json_data()
        return {}

class ReportData:
    def __init__(self,gpd):
        self.of = ObjectFunc()
        self.limit = -1
        self.sub_datetime_dict = {}
        self.order_list=[]
        self.report_obj = gpd.report_obj
        self.table_model= gpd.table_model
        self.extra_dict = gpd.extra_dict
        self.request = gpd.request
        self.error_dict={}

    def get_filter_data(self):
        filter_list = ReportFilterModel.objects.filter(report_id=(self.report_obj))
        filter_dict = {'1':[],  '3':[],  '4':[],  '5':[],  '6':[],  '7':[],  '10':[],  '11':[]}
        exclude_dict = {'2':[],  '8':[]}
        for filter in filter_list:
            if filter.field_id:
                if filter.field_id.field == 'ForeignKey':
                    field_name = filter.field_id.name + '_id'
                else:
                    field_name = filter.field_id.name
            if filter.filter_type == '1':
                filter_dict[filter.filter_type].append(Q((field_name, filter.value)))
            elif filter.filter_type == '2':
                exclude_dict[filter.filter_type].append(Q((field_name, filter.value)))
            elif filter.filter_type == '3':
                filter_dict[filter.filter_type].append(Q((field_name + '__gt', filter.value)))
            elif filter.filter_type == '4':
                filter_dict[filter.filter_type].append(Q((field_name + '__gte', filter.value)))
            elif filter.filter_type == '5':
                filter_dict[filter.filter_type].append(Q((field_name + '__lt', filter.value)))
            elif filter.filter_type == '6':
                filter_dict[filter.filter_type].append(Q((field_name + '__lte', filter.value)))
            elif filter.filter_type == '7':
                filter_dict[filter.filter_type].append(Q((field_name, filter.value)))
            elif filter.filter_type == '8':
                exclude_dict[filter.filter_type].append(Q((field_name, filter.value)))
            elif filter.filter_type == '9':
                self.limit = int(filter.value)
            elif filter.filter_type == '10' and filter.field_id.field in datetime_fields:
                cur_date = datetime.datetime.today()
                filter_dict[filter.filter_type].append(Q((field_name + '__gte', cur_date - self.get_date_filter_value(filter))))
            elif filter.filter_type == '11' and filter.field_id.field in datetime_fields:
                cur_date = datetime.datetime.today()
                filter_dict[filter.filter_type].append(Q((field_name + '__lte', cur_date + self.get_date_filter_value(filter))))
            elif filter.filter_type == '12':
                self.order_list.append(filter.value + filter.field_id.name)
            elif filter.filter_type == '13':
                self.sub_datetime_dict[filter.field_id]=filter.value
        return (filter_dict, exclude_dict)

    def get_filter_q_data(self, fd, ed):
        fdata = Q()
        edata = Q()
        for q_data in fd['1']:
            fdata &= q_data
        for q_data in ed['2']:
            edata |= q_data
        for q_data in fd['3']:
            fdata &= q_data
        for q_data in fd['4']:
            fdata &= q_data
        for q_data in fd['5']:
            fdata &= q_data
        for q_data in fd['6']:
            fdata &= q_data
        for q_data in fd['7']:
            fdata |= q_data
        for q_data in ed['8']:
            edata &= q_data
        for q_data in fd['10']:
            fdata &= q_data
        for q_data in fd['11']:
            fdata &= q_data
        return (fdata, edata)

    def get_master_queryset(self):
        fd, ed = self.get_filter_data()
        fdata, edata = self.get_filter_q_data(fd, ed)
        ol = self.table_model.objects.filter(fdata).exclude(edata)
        return ol
    def get_date_filter_value(self, filter):
        if filter.date_detail == 'month':
            multiplier = 30
        elif filter.date_detail == 'year':
            multiplier = 365
        elif filter.date_detail == 'week':
            multiplier = 7
        else:
            multiplier = 1
        return datetime.timedelta(days=(int(filter.value) * multiplier))
    

class PieChart(ReportData):

    def check_fields(self):
        check_dict={}
        if self.report_obj:
            gf = self.report_obj.group_by_field_id
            tf = self.report_obj.text_field_id
            vf = self.report_obj.value_field_id
            df = self.report_obj.date_field_id
            if gf:
                check_dict["gf"]={"type_error":"Hata: Grup Alanı Boş Bırakılmalı!"}
            if not tf:
                check_dict["tf"]={"type_error":"Hata: Metin Alanı Boş Bırakılmamalı!"}
            if vf:
                if vf.field not in value_fields:
                    check_dict["vf"]={"type_error":"Hata: Değer Alanı Sayısal Bir Alan Değildir. Lütfen Sayısal Bir Alan Seçiniz!"}
        return check_dict

    def get_data(self):
        object_list=[]
        if self.report_obj and len(self.error_dict)==0:
            object_list = self.get_master_queryset()
            object_list = object_list.values(self.report_obj.text_field_id.name)
            if self.report_obj.value_field_id:
                object_list = object_list.annotate(total_value=(Sum(self.report_obj.value_field_id.name)))
            else:
                object_list = object_list.annotate(total_value=(Count(self.report_obj.value_field_id.name)))
        return object_list

    def get_json_data(self):
        self.error_dict=self.check_fields()
        if len(self.error_dict)==0:
            json_dict = {'dataset': {}}
            temp_list = []
            for obj in self.get_data():
                temp_list.append((obj[self.report_obj.text_field_id.name], obj['total_value']))
            ordered_temp_list=self.get_ordered(temp_list)
            for item in ordered_temp_list:
                if 0 not in json_dict['dataset']:
                    json_dict['dataset'][0] = {'text_data':[item[0]], 'value_data':[item[1]]}
                else:
                    json_dict['dataset'][0]['text_data'].append(item[0])
                    json_dict['dataset'][0]['value_data'].append(item[1])
            json_dict=self.get_titles(json_dict)
            return json_dict
        else:
            return self.error_dict
    
    def get_ordered(self,tl):
        if len(self.order_list)>0:
            tfn=self.report_obj.text_field_id.name
            if tfn in self.order_list:
                tl=sorted(tl, key=(lambda tup: tup[0]))
            elif "-%s" % tfn in self.order_list:
                tl=sorted(tl, key=(lambda tup: tup[0]), reverse=True)
            vfn=self.report_obj.value_field_id.name
            if vfn in self.order_list:
                tl=sorted(tl, key=(lambda tup: tup[1]))
            elif "-%s" % vfn in self.order_list:
                tl=sorted(tl, key=(lambda tup: tup[1]), reverse=True)
            if self.limit!=-1:
                return tl[:self.limit]
            elif len(tl)>10:
                return tl[:10]
            else:
                return tl
        else:
            return sorted(tl, key=(lambda tup: tup[1]), reverse=True)

    def get_titles(self, jd):
        jd['title'] = ''
        jd['report_title'] = self.report_obj.title
        jd['group_to_table'] = getattr(self.report_obj.group_by_field_id, 'to') if hasattr(self.report_obj.group_by_field_id, 'to') else ''
        jd['group_to_field'] = getattr(self.report_obj.group_by_field_id, 'name') if hasattr(self.report_obj.group_by_field_id, 'name') else ''
        jd['text_to_table'] = getattr(self.report_obj.text_field_id, 'to') if hasattr(self.report_obj.text_field_id, 'to') else ''
        jd['text_to_field'] = getattr(self.report_obj.text_field_id, 'name') if hasattr(self.report_obj.text_field_id, 'name') else ''
        jd['text_title'] = getattr(self.report_obj.value_field_id, 'verbose_name') if hasattr(self.report_obj.value_field_id, 'verbose_name') else ''
        jd['value_to_table'] = getattr(self.report_obj.value_field_id, 'to') if hasattr(self.report_obj.value_field_id, 'to') else ''
        jd['value_to_field'] = getattr(self.report_obj.value_field_id, 'name') if hasattr(self.report_obj.value_field_id, 'name') else ''
        jd['value_title'] = getattr(self.report_obj.value_field_id, 'verbose_name') if hasattr(self.report_obj.value_field_id, 'verbose_name') else ''
        jd['report_type'] = self.report_obj.report_type
        jd['report_code'] = self.report_obj.code
        if jd['group_to_table'] != '' and jd['group_to_table'] != None:
            gt_model = self.of.get_table_model(self.report_obj.group_by_field_id.to)
        else:
            gt_model = None
        if jd['text_to_table'] != '' and jd['text_to_table'] != None:
            tt_model = self.of.get_table_model(jd['text_to_table'])
        else:
            tt_model = None
        for gkey in jd['dataset']:
            if gt_model != None:
                gtitle = get_object_or_404(gt_model, pk=(int(gkey)))
                jd['dataset'][gkey]['title'] = str(gtitle)
            jd['dataset'][gkey]['text_title'] = jd['dataset'][gkey]['text_data']
        for gkey in jd['dataset']:
            if tt_model != None:
                jd['dataset'][gkey]['text_title'] = []
                for tkey in jd['dataset'][gkey]['text_data']:
                    ttitle = get_object_or_404(tt_model, pk=(int(tkey)))
                    jd['dataset'][gkey]['text_title'].append(str(ttitle))
        return jd
