# -*- coding: utf-8 -*-
from datetime import datetime
from django.http import request
from django.shortcuts import redirect,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from functions.TableFuncs import ObjectFunc
from functions.QuerySetFuncs import ModelQueryset
from authentication.models import OperationHistoryModel
from parameters.models import OperationTypeModel



class GlobalListView(ListView):
	template_name = "global_list.html"
	paginate_by = 50
	action = "List"
	fields = []
	
	def get_extras(self):
		extra_dict = {}
		for item in self.request.GET:
			extra_dict[item] = self.request.GET[item]
		return extra_dict
	
	def get_queryset(self):
		mq = ModelQueryset(self.request,self.kwargs["table_name"],self.action)
		object_list = mq.get_queryset()
		self.field_list=mq.get_table_field_list(mq.table_obj,self.action)
		return object_list
	
	def get_context_data(self, *, object_list=None, **kwargs):
		mq = ModelQueryset(self.request,self.kwargs["table_name"],self.action)
		context = super(GlobalListView, self).get_context_data()
		context["table_name"] = mq.table_obj.name
		context["title"] = mq.table_obj.list_title
		context["fields"] = self.field_list
		return context


class GlobalDetailView(DetailView):
	template_name = "global_detail.html"
	action = "Detail"
	fields = []
	
	def get_queryset(self):
		mq = ModelQueryset(self.request,self.kwargs["table_name"],self.action,fd={"id":self.kwargs["pk"]})
		object_list = mq.get_queryset()
		self.field_list=mq.get_table_field_list(mq.table_obj,self.action)
		return object_list
	
	def get_context_data(self, **kwargs):
		mq = ModelQueryset(self.request,self.kwargs["table_name"],self.action)
		context = super(GlobalDetailView, self).get_context_data()
		context["title"] = mq.table_obj.detail_title % self.object
		context["table_name"] = mq.table_obj.name
		context["list_title"] = mq.table_obj.list_title
		context["fields"] = self.field_list
		context["related_fields"] = mq.get_related_table_list(mq.table_obj)
		return context


class GlobalCreateView(CreateView):
	template_name = "global_form.html"
	action = "Create"
	model_obj = None
	fields = []
	field_list = None
	
	def get_queryset(self):
		mq = ModelQueryset(self.request,self.kwargs["table_name"],self.action)
		object_list = mq.get_queryset()
		self.field_list=mq.get_table_field_list(mq.table_obj,self.action)
		self.fields=[field.name for field in self.field_list]
		return object_list
	
	def get_context_data(self, **kwargs):
		mq = ModelQueryset(self.request,self.kwargs["table_name"],self.action)
		context = super(GlobalCreateView, self).get_context_data()
		context["form_title"] = mq.table_obj.form_title % "Yeni"
		context["title"] = mq.table_obj.form_title % "Yeni"
		context["field_list"] = self.field_list
		context["table_name"] = mq.table_obj.name
		context["list_title"] = mq.table_obj.list_title
		return context
	
	def form_valid(self, form):
		self.object = form.save()
		self.object.save()
		return super().form_valid(form)
	
	def get_success_url(self):
		self.create_log()
		return redirect("global_detail", table_name=self.object.__class__.__name__, pk=self.object.id).url
	
	def get_initial(self):
		initial_dict = super(GlobalCreateView, self).get_initial()
		for item in self.request.GET:
			initial_dict[item] = self.request.GET.get(item)
		return initial_dict
	
	def get_field(self,field_name):
		for field in self.field_list:
			if field.name==field_name:
				return field
		return None

	def get_form(self, form_class=None):
		form = super(GlobalCreateView, self).get_form(form_class)
		for field_name, form_field in form.fields.items():
			form_field.widget.attrs["class"] = "form-control"
			field=self.get_field(field_name)
			if field.field == "DateField":
				form_field.widget.attrs["data-toggle"] = "datetimepicker"
				form_field.widget.attrs["data-target"] = "#id_" + field_name
				form_field.widget.attrs["class"] += " datetimepicker form-date"
			elif field.field == "TimeField":
				form_field.widget.attrs["data-toggle"] = "datetimepicker"
				form_field.widget.attrs["data-target"] = "#id_" + field_name
				form_field.widget.attrs["class"] += " datetimepicker form-time"
			elif field.field == "DateTimeField":
				form_field.widget.attrs["data-toggle"] = "datetimepicker"
				form_field.widget.attrs["data-target"] = "#id_" + field_name
				form_field.widget.attrs["class"] += " datetimepicker form-date-time"
			elif field.field == "ForeignKey":
				form_field.widget.attrs["class"] += " form-dropdown-select2"
			elif field.field == "BooleanField":
				form_field.widget.attrs["class"] += " form-checkbox-select2"
		return form

	def create_log(self):
		table_name= self.object.__class__.__name__
		of=ObjectFunc()
		table_obj=of.get_table_obj(table_name)
		method = get_object_or_404(OperationTypeModel ,code=self.request.method.lower())
		detail = self.get_form_detail(self.object)
		dt = datetime.now()
		user_id = self.request.user
		oh_obj=OperationHistoryModel.objects.create(table_id=table_obj,primary_key=self.object.id,type_id=method,detail=detail,datetime=dt,user_id=user_id)
		oh_obj.save()

	def get_form_detail(self,obj):
		field_list=[]
		value_list=[]
		if obj:
			for field in obj._meta.get_fields():
				if hasattr(field,"column"):
					if field.name!="id":
						field_list.append(field.name)
						value_list.append(str(getattr(obj,field.name)))
		else:
			return "fields:[], values:[]"
		return "fields:[%s], values:[%s]" % (", ".join(field_list),", ".join(value_list))


class GlobalUpdateView(UpdateView):
	template_name = "global_form.html"
	action = "Update"
	fields = []
	
	def get_queryset(self):
		mq = ModelQueryset(self.request,self.kwargs["table_name"],self.action)
		object_list = mq.get_queryset()
		self.field_list=mq.get_table_field_list(mq.table_obj,self.action)
		self.fields=[field.name for field in self.field_list]
		return object_list
	
	def get_context_data(self, **kwargs):
		mq = ModelQueryset(self.request,self.kwargs["table_name"],self.action)
		context = super(GlobalUpdateView, self).get_context_data()
		context["form_title"] = mq.table_obj.form_title % self.object
		context["title"] = mq.table_obj.form_title % self.object
		context["field_list"] = self.field_list
		context["table_name"] = mq.table_obj.name
		context["list_title"] = mq.table_obj.list_title
		return context
	
	def form_valid(self, form):
		self.object = form.save()
		return super().form_valid(form)
	
	def get_success_url(self):
		self.create_log()
		return redirect("global_detail", table_name=self.object.__class__.__name__, pk=self.object.id).url
	
	def get_field(self,field_name):
		for field in self.field_list:
			if field.name==field_name:
				return field
		return None
	
	def get_form(self, form_class=None):
		form = super(GlobalUpdateView, self).get_form(form_class)
		for field_name, form_field in form.fields.items():
			form_field.widget.attrs["class"] = "form-control"
			field=self.get_field(field_name)
			if field.field == "DateField":
				form_field.widget.attrs["data-toggle"] = "datetimepicker"
				form_field.widget.attrs["data-target"] = "#id_" + field_name
				form_field.widget.attrs["class"] += " datetimepicker form-date"
			elif field.field == "TimeField":
				form_field.widget.attrs["data-toggle"] = "datetimepicker"
				form_field.widget.attrs["data-target"] = "#id_" + field_name
				form_field.widget.attrs["class"] += " datetimepicker form-time"
			elif field.field == "DateTimeField":
				form_field.widget.attrs["data-toggle"] = "datetimepicker"
				form_field.widget.attrs["data-target"] = "#id_" + field_name
				form_field.widget.attrs["class"] += " datetimepicker form-date-time"
			elif field.field == "ForeignKey":
				form_field.widget.attrs["class"] += " form-dropdown-select2"
			elif field.field == "BooleanField":
				form_field.widget.attrs["class"] += " form-checkbox-select2"
		return form

	def create_log(self):
		table_name= self.object.__class__.__name__
		of=ObjectFunc()
		table_obj=of.get_table_obj(table_name)
		method = get_object_or_404(OperationTypeModel ,code=self.request.method.lower())
		detail = self.get_form_detail(self.object)
		dt = datetime.now()
		user_id = self.request.user
		oh_obj=OperationHistoryModel.objects.create(table_id=table_obj,primary_key=self.object.id,type_id=method,detail=detail,datetime=dt,user_id=user_id)
		oh_obj.save()

	def get_form_detail(self,obj):
		field_list=[]
		value_list=[]
		if obj:
			for field in obj._meta.get_fields():
				if hasattr(field,"column"):
					if field.name!="id":
						field_list.append(field.name)
						value_list.append(getattr(obj,field.name))
		else:
			return "fields:[], values:[]"
		return "fields:[%s], values:[%s]" % (", ".join(field_list),", ".join(value_list))


class GlobalDeleteView(DeleteView):
	template_name = "global_delete.html"
	action = "Delete"
		
	def get_queryset(self):
		mq = ModelQueryset(self.request,self.kwargs["table_name"],self.action)
		object_list = mq.get_queryset()
		self.field_list=mq.get_table_field_list(mq.table_obj,self.action)
		return object_list
	
	def get_context_data(self, **kwargs):
		mq = ModelQueryset(self.request,self.kwargs["table_name"],self.action)
		context = super(GlobalDeleteView, self).get_context_data()
		context["delete_title"] = mq.table_obj.form_title % self.object
		context["title"] = mq.table_obj.form_title % self.object
		context["table_name"] = mq.table_obj.name
		context["list_title"] = mq.table_obj.list_title
		return context
	
	def get_success_url(self):
		self.create_log()
		return redirect("HomePage").url

	def create_log(self):
		table_name= self.object.__class__.__name__
		of=ObjectFunc()
		table_obj=of.get_table_obj(table_name)
		method = get_object_or_404(OperationTypeModel ,code=self.request.method.lower())
		detail = self.get_form_detail(self.object)
		dt = datetime.now()
		user_id = self.request.user
		oh_obj=OperationHistoryModel.objects.create(table_id=table_obj,primary_key=self.object.id,type_id=method,detail=detail,datetime=dt,user_id=user_id)
		oh_obj.save()

	def get_form_detail(self,obj):
		field_list=[]
		value_list=[]
		if obj:
			for field in obj._meta.get_fields():
				if hasattr(field,"column"):
					if field.name!="id":
						field_list.append(field.name)
						value_list.append(getattr(obj,field.name))
		else:
			return "fields:[], values:[]"
		return "fields:[%s], values:[%s]" % (", ".join(field_list),", ".join(value_list))

