# -*- coding: utf-8 -*-
from django.apps import apps
from django.db.models import Q
import operator,datetime


AppModel=apps.get_model("schema","AppModel")
TableModel=apps.get_model("schema","TableModel")
FieldModel=apps.get_model("schema","FieldModel")
PathModel=apps.get_model("schema","PathModel")

class ObjectFunc:
		
	def get_table_field_list(self,table_obj,purpose):
		field_list = []
		if type(table_obj)==str:
			table_obj=self.get_table_obj(table_obj)
		if type(table_obj)==TableModel:
			purpose_dict = {"List": "show_list", "Detail": "show_detail", "Create": "form_create", "Update": "form_update",
							"Delete": "form_delete"}
			if purpose == "All":
				field_list=FieldModel.objects.filter(table_id=table_obj)
			elif purpose=="List":
				field_list=FieldModel.objects.filter(table_id=table_obj).filter(show_list=True)
			elif purpose=="Detail":
				field_list=FieldModel.objects.filter(table_id=table_obj).filter(show_detail=True)
			elif purpose=="Create":
				field_list=FieldModel.objects.filter(table_id=table_obj).filter(form_create=True)
			elif purpose=="Update":
				field_list=FieldModel.objects.filter(table_id=table_obj).filter(form_update=True)
			elif purpose=="Delete":
				field_list=FieldModel.objects.filter(table_id=table_obj).filter(form_delete=True)
			else:
				field_list=[]
			field_list = sorted(field_list, key=operator.attrgetter("order"))
		else:
			print("Model Objesi Bulunamadı(Field) %s" % table_obj.name)
		return field_list
	
	def get_related_table_list(self,table_obj):
		table_list=FieldModel.objects.filter(to=table_obj.name)
		return table_list
	
	def get_table_obj(self,table_name):
		if type(table_name)==str:
			table_list = TableModel.objects.filter(name=table_name)
			if len(table_list)==1:
				return table_list[0]
		print("Tablo Objesi Bulunamadı(Tablo Obj) %s" % table_name)
		return table_list
	
	def get_table_model(self,table_obj):
		if type(table_obj)==str:
			table_obj=self.get_table_obj(table_obj)
		if type(table_obj)==TableModel:
			return apps.get_model(table_obj.app_id.name, table_obj.name)
		else:
			print("Tablo Objesi Bulunamadı(Tablo) %s" % table_obj)
		return None
	
	def get_app(self,app_name):
		if type(app_name)==str:
			app_list = AppModel.objects.filter(name=app_name)
			if len(app_list)==1:
				return app_list[0]
		print("Uygulama Bulunamadı %s" % app_name)
		return None
	
	def get_path(self,path_name):
		if type(path_name)==str:
			path_list = PathModel.objects.filter(name=path_name)
			if len(path_list)==1:
				return path_list[0]
		print("Güzergah Bulunamadı %s" % path_name)
		return None

	def get_field_obj(self,table_name,field_name):
		table_obj=self.get_table_obj(table_name)
		field_list=self.get_table_field_list(table_obj,"All")
		for field in field_list:
			if field.name==field_name:
				return field
		return None
  
class AttrDict(ObjectFunc):
	def __init__(self,object):
		super(AttrDict, self).__init__()
		self.m_name=object.__class__.__name__
		self.table_obj=self.get_table_obj(self.m_name)
		self.table_model=self.get_table_model(self.table_obj)
		self.object=object

	def get_attr_dict(self,purpose):
		attr_dict={}
		for field in self.get_table_field_list(self.table_obj,purpose):
			attr_dict[field.name]=getattr(self.object,field.name)
		return attr_dict
	
	def get_ajax_dict(self,purpose):
		ajax_dict={}
		for field in self.get_table_field_list(self.table_obj,purpose):
			value=getattr(self.object,field.name)
			if field.field=="ForeignKey" and value:
				ajax_dict[field.name]=str(value.id)
			else:
				ajax_dict[field.name]=str(value)
		return ajax_dict

	def get_remote_attr_dict(self):
		remote_attr_dict={}
		field_model=apps.get_model("main","FieldLM")
		remote_model_list=[field for field in field_model.objects.filter(to=self.model_obj.name)]
		for field in remote_model_list:
			remote_attr_dict[field]=[value for value in getattr(self.object,"%s_set" % field.model.name.lower()).all()][:10]
		return remote_attr_dict

