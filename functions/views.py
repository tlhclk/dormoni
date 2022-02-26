# -*- coding: utf-8 -*-
from django.shortcuts import redirect,render
from django.views.generic import FormView,ListView,DetailView,View
from .other.to_export import ExportData

class ToExportView(View):
    template_name="function/to_export.html"

    def get_context_data(self):
        ed=ExportData()
        ed.ready()
        context_data = {}
        context_data['title'] = 'Program Şemasını Veritabanına Kaydetme'
        return context_data

    def get(self, request):
        return render(request, (self.template_name), context=(self.get_context_data()))

