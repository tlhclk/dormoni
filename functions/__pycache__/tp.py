# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\functions\TemplateFuncs.py
# Compiled at: 2022-01-10 12:16:03
# Size of source mod 2**32: 9504 bytes
from typing import NoReturn
from authentication.models import AuthenticationUserModel
from functions.TableFuncs import ObjectFunc
from functions.QuerySetFuncs import ModelQueryset
from financial.models import RepetitiveTransactionModel, ChangeTransactionModel
from main.models import ReportModel
from note.models import NoteRecordModel
from note.forms import NoteForm
from django import template
from datetime import datetime, timedelta
import math
register = template.Library()

@register.filter(name='GetAttrValue')
def GetAttrValue(obj, field):
    output = ''
    if hasattr(obj, field.name):
        value = getattr(obj, field.name)
        if not value:
            return ''
            if field.field == 'CharField':
                output = value[:100]
        elif field.field == 'ForeignKey':
            output = "<a href='/global_detail/%s/%d/'>%s</a>" % (field.to, value.id, value)
        else:
            if field.field == 'DateField':
                output = value.strftime('%Y-%m-%d')
            else:
                if field.field == 'TimeField':
                    output = value.strftime('%H:%M:%S')
                else:
                    if field.field == 'DateTimeField':
                        output = value.strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        if field.field == 'BooleanField':
                            if value:
                                output = 'Evet'
                        else:
                            output = 'Hayır'
    else:
        if field.field == 'DecimalField':
            output = value
        else:
            if field.field == 'IntegerField':
                output = value
            else:
                if field.field == 'EmailField':
                    output = value
                else:
                    try:
                        output = value[:100]
                    except:
                        pass
                    else:
                        return output


@register.filter(name='GetRelatedAttrValue')
def GetRelatedAttrValue(obj, field):
    if field.related_name != '' and field.related_name != None:
        print(type(field.related_name))
        object_list = getattr(obj, '%s' % field.related_name).all()[:10]
    else:
        object_list = getattr(obj, '%s_set' % field.table_id.name.lower()).all()[:10]
    return object_list


@register.filter(name='getValue')
def getValue(dict_obj, field):
    if field in dict_obj:
        return dict_obj[field]
    return ''


@register.inclusion_tag('partial_html/sidebar.html')
def GetSidebarMenu(request):
    table_menu = {}
    path_menu = {}
    listname = ''
    if request.user.is_superuser:
        listname = 'admin'
    else:
        listname = 'master_user'
    mq = ModelQueryset(request, 'PathModel', 'List', fd={'type_id_id__in':[6, 7, 8],  'location':listname})
    path_list = mq.get_queryset()
    for path in path_list:
        if path.type_id_id == 8:
            if path.app_id.verbose_name not in path_menu:
                path_menu[path.app_id.verbose_name] = []
            path_menu[path.app_id.verbose_name].append(path)
        else:
            if path.type_id.name not in path_menu:
                path_menu[path.type_id.name] = []
            path_menu[path.type_id.name].append(path)
    else:
        return {'path_menu':path_menu, 
         'table_menu':table_menu}


@register.inclusion_tag('partial_html/table_pagination.html')
def GetTablePagination(request):
    base_url = request.META['PATH_INFO']
    table_name = request.resolver_match.kwargs['table_name']
    of = ObjectFunc()
    table_model = of.get_table_model(of.get_table_obj(table_name))
    last_page = math.ceil(len(table_model.objects.all()) / 50)
    if 'page' in request.GET:
        cur_page = int(request.GET['page'])
    else:
        cur_page = 1
    first_page = 1
    prev_page = cur_page - 1
    next_page = cur_page + 1
    page_list = []
    for i in range(cur_page - 3, cur_page + 4):
        if i <= last_page:
            if i >= first_page:
                page_list.append(i)
            if first_page in page_list:
                if page_list[0] == cur_page:
                    first_page = 0
                else:
                    del page_list[0]
            if last_page in page_list:
                if page_list[(-1)] == cur_page:
                    last_page = 0
                else:
                    del page_list[-1]
            if prev_page <= first_page:
                prev_page = 0
            if next_page >= last_page:
                next_page = 0
        return {'first_page':first_page, 
         'cur_page':cur_page,  'last_page':last_page,  'prev_page':prev_page,  'next_page':next_page,  'page_list':page_list,  'table_name':table_name}


@register.inclusion_tag('partial_html/detail_pagination.html')
def GetDetailPagination(request):
    table_name = request.resolver_match.kwargs['table_name']
    mq = ModelQueryset(request, table_name, 'Detail')
    table_model = mq.get_table_model(table_name)
    obj_list = mq.get_queryset()
    primary_key = int(request.resolver_match.kwargs['pk'])
    obj = table_model.objects.get(pk=primary_key)
    index_no = list(obj_list.values_list('id', flat=True)).index(obj.id)
    if index_no > 0:
        next_obj = obj_list[(index_no - 1)].id
    else:
        next_obj = 0
    if index_no < len(obj_list) - 1:
        prev_obj = obj_list[(index_no + 1)].id
    else:
        prev_obj = 0
    return {'primary_key':primary_key, 
     'table_name':table_name,  'prev_obj':prev_obj,  'next_obj':next_obj}


@register.inclusion_tag('partial_html/notes.html')
def GetNotes(request):
    table_name = request.resolver_match.kwargs['table_name']
    primary_key = int(request.resolver_match.kwargs['pk'])
    mq = ModelQueryset(request, table_name, 'Detail')
    table_obj = mq.get_table_obj(table_name)
    note_record_list = NoteRecordModel.objects.filter(table_id=table_obj, primary_key=primary_key)
    return {'note_list': note_record_list}


@register.inclusion_tag('partial_html/note_form.html')
def GetNoteForm():
    note_form = NoteForm()
    return {'note_form': note_form}


@register.simple_tag
def GetProfilePic(request):
    if not request.user.is_anonymous:
        obj = AuthenticationUserModel.objects.get(user_id_id=(request.user.id))
        return obj.profile_pic
    return ''


@register.inclusion_tag('partial_html/transaction_pie_chart.html')
def GetFinancialReportCard(table_name, date_interval, date_count, text_field, value_field, date_field, type_id):
    data = {'table_name':table_name,  'date_interval':date_interval,  'date_count':date_count,  'text_field':text_field,  'value_field':value_field,  'date_field':date_field,  'type_id':type_id}
    print(data)
    data['report_title'] = 'hoşt'
    return data


@register.inclusion_tag('partial_html/global_chart.html')
def GetReport(request, report_code):
    data = {}
    report = ReportModel.objects.get(code=report_code)
    data['report'] = report
    return data


@register.inclusion_tag('partial_html/ChangeModelDetail.html')
def GetChangeModelDetail(request):
    payment_data = {'sum': {'str':str('Toplam'),  'paid':0,  'unpaid':0,  'balance':0,  'rate':0}}
    path = request.path
    path_list = path.split('/')
    pk = path_list[(-2)]
    ct_list = ChangeTransactionModel.objects.filter(change_id_id=(int(pk)))
    for obj in ct_list:
        trn = obj.transaction_id
        ac = trn.account_id
        if ac.id not in payment_data:
            payment_data[ac.id] = {'str':str(ac), 
             'paid':0,  'unpaid':0,  'balance':0,  'rate':0}
            if trn.type_id_id == 1:
                payment_data[ac.id]['paid'] = trn.amount
                payment_data['sum']['paid'] += trn.amount
            else:
                payment_data[ac.id]['unpaid'] = trn.amount
                payment_data['sum']['unpaid'] += trn.amount
        elif trn.type_id_id == 1:
            payment_data[ac.id]['paid'] += trn.amount
            payment_data['sum']['paid'] += trn.amount
        else:
            payment_data[ac.id]['unpaid'] += trn.amount
            payment_data['sum']['unpaid'] += trn.amount
    else:
        for ac_id in payment_data:
            if payment_data[ac_id]['paid'] > payment_data[ac_id]['unpaid']:
                payment_data[ac_id]['balance'] = '%s Miktar: %f' % ('Alınacak', payment_data[ac_id]['paid'] - payment_data[ac_id]['unpaid'])
                payment_data[ac_id]['rate'] = round(payment_data[ac_id]['unpaid'] / payment_data[ac_id]['paid'] * 100, 2) if payment_data[ac_id]['paid'] != 0 else 0
            else:
                payment_data[ac_id]['balance'] = '%s Miktar: %f' % ('Verilecek', payment_data[ac_id]['unpaid'] - payment_data[ac_id]['paid'])
                payment_data[ac_id]['rate'] = round(payment_data[ac_id]['paid'] / payment_data[ac_id]['unpaid'] * 100, 2) if payment_data[ac_id]['unpaid'] != 0 else 0
        else:
            context_data = {'payment_data': payment_data}
            return context_data


@register.inclusion_tag('partial_html/RepetitiveModelDetail.html')
def GetRepetitiveModelDetail(request):
    payment_data = []
    path = request.path
    path_list = path.split('/')
    pk = path_list[(-2)]
    inter_val = 0
    max_value = 0
    min_value = 0
    rt_list = RepetitiveTransactionModel.objects.filter(repetitive_id_id=(int(pk))).order_by('-id')
    r_obj = rt_list[0].repetitive_id if len(rt_list) > 0 else None
    for obj in rt_list:
        if len(payment_data) < 10:
            payment_data.append({'from_value':obj.start_date.strftime('%Y-%m-%d'),  'to_value':obj.end_date.strftime('%Y-%m-%d'),  'last_date':obj.last_date,  'amount':obj.transaction_id.amount,  'id':obj.id,  'start_date':obj.start_date,  'end_date':obj.end_date})
        if r_obj:
            if r_obj.period_id_id == 1:
                inter_val = float(r_obj.period_amount) * 365 * 10
                max_value = (datetime.today() + timedelta(days=90)).strftime('%Y-%m-%d')
                min_value = (datetime.today() - timedelta(days=90) - timedelta(days=inter_val)).strftime('%Y-%m-%d')
            else:
                if r_obj.period_id_id == 2:
                    inter_val = float(r_obj.period_amount) * 365
                    max_value = (datetime.today() + timedelta(days=30)).strftime('%Y-%m-%d')
                    min_value = (datetime.today() - timedelta(days=30) - timedelta(days=inter_val)).strftime('%Y-%m-%d')
                else:
                    if r_obj.period_id_id == 3:
                        inter_val = 36500
                        max_value = (datetime.today() + timedelta(days=21)).strftime('%Y-%m-%d')
                        min_value = (datetime.today() - timedelta(days=21) - timedelta(days=inter_val)).strftime('%Y-%m-%d')
                    else:
                        if r_obj.period_id_id == 4:
                            inter_val = float(r_obj.period_amount) * 1 * 10
                            max_value = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
                            min_value = (datetime.today() - timedelta(days=7) - timedelta(days=inter_val)).strftime('%Y-%m-%d')
        context_data = {'payment_data':payment_data, 
         'inter_val':inter_val,  'min_value':min_value,  'max_value':max_value}
        return context_data