# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from django.views.generic import View
from toexport.apps import ExportData


class IndexPage(View):
	template_name = "base.html"
	
	def get_context_data(self):
		context_data = {}
		context_data["title"] = "Hoş Geldiniz"
		return context_data

	def get(self, request):
		return render(request, self.template_name, context=self.get_context_data())

class HomePage(View):
	template_name = "home.html"
	
	def get_context_data(self):
		context_data = {}
		context_data["title"] = "Ana Sayfa"
		return context_data

	def get(self, request):
		return render(request, self.template_name, context=self.get_context_data())

class ToexportPage(View):
	template_name = "toexport.html"
	
	def get_context_data(self):
		context_data = {}
		context_data["title"] = "Tabloları Dışa Aktar"
		return context_data

	def get(self, request):
		ExportData().ready()
		return render(request, self.template_name, context=self.get_context_data())
