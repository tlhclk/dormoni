from django.shortcuts import render
from django.views.generic import View
from django.apps import apps
from django.urls import *
import xlwt,inspect
# Create your views here.




class CollectModels:
    def __init__(self):
        self.model_wb=xlwt.Workbook()
        self.field_wb=xlwt.Workbook()
        self.path_wb=xlwt.Workbook()
        self.data_wb=xlwt.Workbook()
        self.model_wb_name="django_model_wb.xls"
        self.field_wb_name="django_field_wb.xls"
        self.path_wb_name="django_path_wb.xls"
        self.data_wb_name="django_data_wb.xls"

    def run(self):
        print("İşlem Başlatıldı")
        all_models = apps.get_models()
        self.model_info(all_models)

    def run2(self):
        print("İşlem Başlatıldı")
        url_patterns=get_resolver().url_patterns
        pattern_list=self.path_info(url_patterns)
        for pattern in pattern_list:
            print(pattern.pattern,pattern.callback,pattern.name)
            try:
                print("View init: %s" % pattern.callback.initkwargs)
                print(inspect.getsource(pattern.callback.view_class))
            except AttributeError or OSError:
                pass



    def path_info(self,url_patterns):
        pattern_list=[]
        try:
            print(url_patterns.__dict__)
        except AttributeError:
            pass
        for pattern in url_patterns:
            if hasattr(pattern,"url_patterns"):
                path_list=self.path_info(pattern.url_patterns)
                pattern_list+=path_list
            else:
                pattern_list.append(pattern)
        return pattern_list


    def model_info(self,data):
        title_dict={"__module__":0,"__str__":1,"objects":2,"_meta":3}
        field_list=[]
        sht0 = self.model_wb.add_sheet("model_info")
        for y,model_data in enumerate(data):
            try:
                print(model_data.__name__)
                value = model_data.__module__
                sht0.write(y+1,1,str(value))
                value2 = inspect.getsource(model_data.__str__).strip().replace("\n","\\n").replace("    ","\\t")
                sht0.write(y+1,2,str(value2))
                value3 = model_data._meta.db_table
                sht0.write(y+1,3,str(value3))
                value4 = model_data._meta.ordering
                sht0.write(y+1,4,str(value4))
                value5 = model_data._meta.model_class
                sht0.write(y+1,5,str(value5))
                value6 = model_data._meta.__name__
                sht0.write(y+1,6,str(value6))
                field_list.append(model_data._meta.fields)
            except AttributeError:
                pass
        self.model_wb.save(self.model_wb_name)


class ToExportView(View):
    template_name = "index.html"

    def get_context_data(self):
        context_data = {}
        context_data["title"] = "İşlem Kayıtları"
        return context_data

    def get(self, request):
        return render(request, self.template_name, context=self.get_context_data())