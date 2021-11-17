# -*- coding: utf-8 -*-
from typing import NoReturn
from authentication.models import AuthenticationUserModel
from functions.TableFuncs import ObjectFunc
from functions.QuerySetFuncs import ModelQueryset
from schema.models import PathModel, TableModel
from note.models import NoteRecordModel
from note.forms import NoteForm
from django import template
import math

register = template.Library()

@register.filter(name='GetAttrValue')
def GetAttrValue(obj,field):
	output = ""
	if hasattr(obj,field.name):
		value = getattr(obj,field.name)
		if not value:
			return ""
		if field.field == "CharField":
			output = value[:100]
		elif field.field == "ForeignKey":
			output = "<a href='/global_detail/%s/%d/'>%s</a>" % (field.to,value.id,value)
		elif field.field == "DateField":
			output = value.strftime('%Y-%m-%d')
		elif field.field == "TimeField":
			output = value.strftime('%H:%M:%S')
		elif field.field == "DateTimeField":
			output = value.strftime('%Y-%m-%d %H:%M:%S')
		elif field.field == "BooleanField":
			if value:
				output="Evet"
			else:
				output="Hayır"
		elif field.field == "DecimalField":
			output = value
		elif field.field == "IntegerField":
			output = value
		elif field.field == "EmailField":
			output = value
		else:
			try:
				output = value[:100]
			except:
				pass
	return output

@register.filter(name='GetRelatedAttrValue')
def GetRelatedAttrValue(obj,field):
	object_list=getattr(obj,"%s_set" % field.table_id.name.lower()).all()[:10]
	return object_list

@register.inclusion_tag("partial_html/sidebar.html")
def GetSidebarMenu(request):
	table_menu = {}
	path_menu = {}
	listname=""
	if request.user.is_superuser:
		listname="admin"
	else:
		listname="master_user"
	mq=ModelQueryset(request,"PathModel","List",fd={"type_id_id__in":[6,7,8],"location":listname})
	path_list=mq.get_queryset()
	# for table in table_list:
	# 	if table.app_id.type_id_id==1:# apps türündeki uygulamalar
	# 		if table.app_id.verbose_name not in table_menu:
	# 			table_menu[table.app_id.verbose_name]=[]
	# 		table_menu[table.app_id.verbose_name].append(table)
	for path in path_list:
		if path.type_id_id==8:
			if path.app_id.verbose_name not in path_menu:
				path_menu[path.app_id.verbose_name]=[]
			path_menu[path.app_id.verbose_name].append(path)
		else:
			if path.type_id.name not in path_menu:
				path_menu[path.type_id.name]=[]
			path_menu[path.type_id.name].append(path)
	return {"path_menu":path_menu,"table_menu":table_menu}

@register.inclusion_tag("partial_html/table_pagination.html")
def GetTablePagination(request):
	base_url=request.META["PATH_INFO"]
	table_name=request.resolver_match.kwargs["table_name"]
	of=ObjectFunc()
	table_model=of.get_table_model(of.get_table_obj(table_name))
	last_page=math.ceil(len(table_model.objects.all())/50)
	if "page" in request.GET:
		cur_page=int(request.GET["page"])
	else:
		cur_page=1
	first_page=1
	prev_page=cur_page-1
	next_page=cur_page+1
	page_list=[]
	for i in range(cur_page-3,cur_page+4):
		if i<=last_page and i>=first_page:
			page_list.append(i)
	if first_page in page_list:
		if page_list[0]==cur_page:
			first_page=0
		else:
			del page_list[0]
	if last_page in page_list:
		if page_list[-1]==cur_page:
			last_page=0
		else:
			del page_list[-1]
	if prev_page<=first_page:
		prev_page=0
	if next_page>=last_page:
		next_page=0
	return {"first_page":first_page,"cur_page":cur_page,"last_page":last_page,"prev_page":prev_page,"next_page":next_page,"page_list":page_list,"table_name":table_name}

@register.inclusion_tag("partial_html/detail_pagination.html")
def GetDetailPagination(request):
	table_name=request.resolver_match.kwargs["table_name"]
	mq=ModelQueryset(request,table_name,"Detail")
	table_model=mq.get_table_model(table_name)
	obj_list=mq.get_queryset()
	primary_key=int(request.resolver_match.kwargs["pk"])
	obj=table_model.objects.get(pk=primary_key)
	index_no=list(obj_list.values_list('id', flat=True)).index(obj.id)
	if index_no>0:
		next_obj=obj_list[index_no-1].id 
	else: 
		next_obj=0
	if index_no<len(obj_list)-1:
		prev_obj=obj_list[index_no+1].id 
	else: 
		prev_obj=0
	return {"primary_key":primary_key,"table_name":table_name,"prev_obj":prev_obj,"next_obj":next_obj}
		
@register.inclusion_tag("partial_html/notes.html")
def GetNotes(request):
	table_name=request.resolver_match.kwargs["table_name"]
	primary_key=int(request.resolver_match.kwargs["pk"])
	mq=ModelQueryset(request,table_name,"Detail")
	table_obj=mq.get_table_obj(table_name)
	note_record_list=NoteRecordModel.objects.filter(table_id=table_obj,primary_key=primary_key)
	return {"note_list":note_record_list}

@register.inclusion_tag("partial_html/note_form.html")
def GetNoteForm():
	note_form=NoteForm()
	return {"note_form":note_form}

@register.simple_tag
def GetProfilePic(request):
	if not request.user.is_anonymous:
		obj=AuthenticationUserModel.objects.get(user_id_id=request.user.id)
		return obj.profile_pic
	return ""