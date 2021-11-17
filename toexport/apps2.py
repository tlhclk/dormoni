from django.apps import AppConfig, apps
from django.urls import *
from django.conf import settings
import xlwt,inspect, types,builtins,os


class ExportData:
    app_data = True
    table_data = True
    field_data = True
    path_data = True
    import_data = True
    data_data = True
    def __init__(self):
        self.app_wb=xlwt.Workbook()
        self.app_wb_name="schema_app.xls"
        self.shta=self.app_wb.add_sheet("schema_app")
        self.ax,self.ay=0,1
        if self.table_data:
            self.table_wb=xlwt.Workbook()
            self.table_wb_name="schema_table.xls"
            self.shtt=self.table_wb.add_sheet("schema_table")
            self.tx,self.ty=0,1
        if self.field_data:
            self.field_wb=xlwt.Workbook()
            self.field_wb_name="schema_field.xls"
            self.shtf=self.field_wb.add_sheet("schema_field")
            self.fx,self.fy=0,1
        if self.path_data:
            self.path_wb=xlwt.Workbook()
            self.path_wb_name="schema_path.xls"
            self.shtp=self.path_wb.add_sheet("schema_path")
            self.px,self.py=0,1
        if self.import_data:
            self.import_wb=xlwt.Workbook()
            self.import_wb_name="schema_import.xls"
            self.shti=self.import_wb.add_sheet("schema_import")
            self.ix,self.iy=0,1
        self.write_headers()
        if os.path.exists(os.getcwd()+"/data"):
            if not os.path.isdir(os.getcwd()+"/data"):
                os.mkdir(os.getcwd()+"/data")
        else:
            os.mkdir(os.getcwd()+"/data")

    def write_headers(self):
        app_header=["#","name","type_id","verbose_name","note_id"]
        for title in app_header:
            self.shta.write(0,self.ax,title)
            self.ax+=1
        if self.table_data:
            table_header=["#","__module__","__str__","db_table","ordering","name","verbose_name","app","order"]
            for title in table_header:
                self.shtt.write(0,self.tx,title)
                self.tx+=1
        if self.field_data:
            key_list=["#","name","verbose_name","field","table","null","blank","max_length","on_delete","to","default",
                      "max_digits","decimal_places","is_generated","show_list","form_create","show_detail","form_update",
                      "form_delete","order","note","is_pk","help_text","error_messages"]
            for key in key_list:
                self.shtf.write(0,self.fx,key)
                self.fx+=1
        if self.path_data:
            path_header=["#","_route","_regex","namespace","app_name","name","parent_namespace"]
            for title in path_header:
                self.shtp.write(0,self.px,title)
                self.px+=1
        if self.import_data:
            import_header=["#","app","file","import_type","from","import"]
            for header in import_header:
                self.shti.write(0,self.ix,header)
                self.ix+=1

    def close(self):
        if self.app_data:
            self.app_wb.save("data/"+self.app_wb_name)
        if self.table_data:
            self.table_wb.save("data/"+self.table_wb_name)
        if self.field_data:
            self.field_wb.save("data/"+self.field_wb_name)
        if self.path_data:
            self.path_wb.save("data/"+self.path_wb_name)
        if self.import_data:
            self.import_wb.save("data/"+self.import_wb_name)

    def code_info(self):
        print("Dışarı Aktarma İşlemi Başladı.")
        app_dict=self.app_info()
        if self.table_data:
            self.table_info()
        if self.path_data:
            self.path_info()
        for app,props in app_dict.items():
            if props["type"]=="apps":
                file_data = self.get_file_data(app)
        self.close()
        print("Dışarı Aktarma işlemi Bitti.")

    def app_info(self):
        print("\tUygulama Bilgileri Ayrıştırılıyor.")
        config_list=apps.get_app_configs()
        root_path=os.getcwd()
        folder_list=[f for f in os.listdir(root_path) if not os.path.isfile(os.path.join(root_path, f))]
        project_name = settings.ROOT_URLCONF.split(".")[0]
        app_dict={}
        for config in config_list:
            app_dict[config.name]={"type":""}
            if hasattr(config,"verbose_name"):
                app_dict[config.name]["verbose_name"]=str(config.verbose_name)
            else:
                app_dict[config.name]["verbose_name"] =""
            if config.name == project_name:
                app_dict[config.name]["type"]="project_core"
            elif config.name in folder_list:
                app_path=os.path.join(root_path, config.name)
                folder_list2=[f for f in os.listdir(app_path) if os.path.isfile(os.path.join(app_path, f))]
                type_list=[f.split(".")[-1] for f in folder_list2]
                if "apps.py" in folder_list2 and "models.py" in folder_list2:
                    app_dict[config.name]["type"]="apps"
                elif "py" in type_list:
                    app_dict[config.name]["type"]="codes"
                else:
                    app_dict[config.name]["type"]="files"
            else:
                app_dict[config.name]["type"]="project_lib"
            self.shta.write(self.ay,0,self.ay)
            self.shta.write(self.ay,1,config.name)
            self.shta.write(self.ay,2,app_dict[config.name]["type"])
            self.shta.write(self.ay,3,app_dict[config.name]["verbose_name"])
            self.ay+=1
        print("\tUygulama Bilgileri Dışarı Aktarıldı.")
        return app_dict

    def table_info(self):
        print("\tTablo Bilgileri Ayrıştırılıyor.")
        all_models = apps.get_models()
        self.field_dict={}
        for model_data in  all_models:
            field_list=[]
            try:
                value = model_data.__module__
                self.shtt.write(self.ty,1,str(value))
                value2 = inspect.getsource(model_data.__str__).strip().replace("\n","\\n").replace("    ","\\t")
                self.shtt.write(self.ty,2,str(value2))
                value3 = model_data._meta.db_table
                self.shtt.write(self.ty,3,str(value3))
                value4 = model_data._meta.ordering
                self.shtt.write(self.ty,4,str(value4))
                value5 = model_data.__name__
                self.shtt.write(self.ty,5,str(value5))
                value6 = model_data._meta.verbose_name
                self.shtt.write(self.ty,6,str(value6))
                value7 = model_data.__module__.split(".")[0]
                self.shtt.write(self.ty,7,str(value7))
                field_list=model_data._meta.fields
                self.shtt.write(self.ty,0,self.ty)
                self.ty+=1
            except AttributeError:
                pass
            self.field_dict[model_data]=field_list
            if self.data_data:
                self.get_all_data(model_data,field_list)
        if self.field_data:
            self.field_info(field_list)
        print("\tTablo Bilgileri Dışarı Aktarıldı.")

    def field_info(self,field_list):
        print("\t\t%s Tablosu Alan Bilgileri Ayrıştırılıyor." % field_list[0].model.__name__)
        model_dict={}
        for field in field_list:
            value1=field.name
            self.shtf.write(self.fy,1,value1)
            value2=str(field.verbose_name)
            self.shtf.write(self.fy,2,value2)
            value3=field.get_internal_type()
            self.shtf.write(self.fy,3,value3)
            value4=field.model.__name__
            self.shtf.write(self.fy,4,value4)
            value5=field.null
            self.shtf.write(self.fy,5,value5)
            value6=field.blank
            self.shtf.write(self.fy,6,value6)
            value7=field.max_length
            self.shtf.write(self.fy,7,value7)
            value8="models.SET_NULL"
            self.shtf.write(self.fy,8,value8)
            if field.get_internal_type()=="ForeignKey":
                value9=field.remote_field.related_model.__name__
            else:
                value9=""
            self.shtf.write(self.fy,9,value9)
            if type(field.default)==bool:
                value10=str(field.default)
            elif type(field.default)==types.FunctionType:
                value10=str(field.default())
            elif type(field.default)==types.BuiltinMethodType:
                value10=str(field.default())
            else:
                value10=""
            self.shtf.write(self.fy,10,value10)
            try:
                value11=field.max_digits
                value12=field.decimal_places
            except AttributeError:
                value11=0
                value12=0
            self.shtf.write(self.fy,11,value11)
            self.shtf.write(self.fy,12,value12)
            value13=False
            self.shtf.write(self.fy,13,value13)
            value14=True
            self.shtf.write(self.fy,14,value14)
            value15=field.editable
            self.shtf.write(self.fy,15,value15)
            value16=True
            self.shtf.write(self.fy,16,value16)
            value17=field.editable
            self.shtf.write(self.fy,17,value17)
            value18=field.editable
            self.shtf.write(self.fy,18,value18)
            if value4 in model_dict:
                model_dict[value4]+=1
            else:
                model_dict[value4]=1
            value19=model_dict[value4]
            self.shtf.write(self.fy,19,value19)
            value20=""
            self.shtf.write(self.fy,20,value20)
            value21=field.primary_key
            self.shtf.write(self.fy,21,value21)
            value22=str(field.help_text)
            self.shtf.write(self.fy,22,value22)
            value23=str(field.error_messages)
            self.shtf.write(self.fy,23,value23)
            self.fy+=1
        print("\t\t%s Tablosu Alan Bilgileri Dışarı Aktarıldı." % field_list[0].model.__name__)

    def path_info(self):
        print("\tGüzergah Bilgileri Ayrıştırılıyor.")
        url_patterns=get_resolver().url_patterns
        self.path_info_recursive(url_patterns,self.shtp)
        print("\tGüzergah Bilgileri Dışarı Aktarıldı.")

    def path_info_recursive(self,url_patterns,sht0,parent_route="",parent_namespace=None):
        for pattern in url_patterns:
            if not pattern.pattern._is_endpoint:
                # include or not
                if pattern.namespace!="admin":
                    if hasattr(pattern.pattern, "_route"):
                        cur_route = pattern.pattern._route
                    else:
                        cur_route=""
                    if type(pattern.urlconf_name)==list:
                        self.path_info_recursive(pattern.urlconf_name,sht0,parent_route+cur_route,pattern.namespace)
                    else:
                        self.path_info_recursive(pattern.urlconf_name.urlpatterns, sht0,parent_route+cur_route,pattern.namespace)
            if hasattr(pattern,"pattern"):
                if hasattr(pattern.pattern,"_route"):
                    value = pattern.pattern._route
                    sht0.write(self.py, 1, str(value))
                else:
                    sht0.write(self.py, 1, str(parent_route))
                if hasattr(pattern.pattern,"_regex"):
                    value2 = pattern.pattern._regex
                    sht0.write(self.py, 2, str(value2))
            if hasattr(pattern,"namespace"):
                value3 = pattern.namespace
                sht0.write(self.py, 3, str(value3))
            if hasattr(pattern,"app_name"):
                value4 = pattern.app_name
                sht0.write(self.py, 4, str(value4))
            if hasattr(pattern,"name"):
                value5 = pattern.name
                sht0.write(self.py, 5, str(value5))
            if parent_namespace:
                sht0.write(self.py, 6, str(parent_namespace))
            sht0.write(self.py, 0, self.py)
            self.py+=1

    def write_import_data(self,app,file,import_data):
        for imp in import_data:
            import_type,fr_data,imp_data = imp
            self.shti.write(self.iy,0,self.ix)
            self.shti.write(self.iy,1,app)
            self.shti.write(self.iy,2,file)
            self.shti.write(self.iy,3,import_type)
            self.shti.write(self.iy,4,fr_data)
            self.shti.write(self.iy,5,imp_data)
            self.iy+=1

    def get_import_data(self,file_data):
        import_list=[]
        for line in file_data:
            line=line.strip()
            line_list=line.split()
            if len(line_list)>0:
                if line_list[0]=="import":
                    import_str="".join(line_list[1:])
                    for i in import_str.split(","):
                        import_list.append(("import","",i.strip()))
                elif line_list[0]=="from":
                    f=line_list[1]
                    import_str="".join(line_list[3:])
                    for i in import_str.split(","):
                        import_list.append(("from",f,i.strip()))
        return import_list
            
    def get_file_data(self,app):
        print("\t%s Uygulaması Dosya Bilgileri Ayrıştırılıyor." % app)
        file_list=["apps","views","serializers","urls","admin","models"]
        for file_name in file_list:
            try:
                root_path=os.getcwd()
                file_path=os.path.join(os.path.join(root_path, app),file_name+".py")
                file_data=open(file_path,"r+")
                if self.import_data:
                    print("\t\t%s Uygulaması %s Dosyası 'import' Bilgileri Ayrıştırılıyor." % (app,file_name))
                    import_data=self.get_import_data(file_data)
                    self.write_import_data(app,file_name,import_data)
                    print("\t\t%s Uygulaması %s Dosyası 'import' Bilgileri Dışarı Aktarıldı." % (app,file_name))
            except FileNotFoundError:
                pass
        print("\t%s Uygulaması Dosya Bilgileri Dışarı Aktarıldı" % app)
        return {}
            
    def get_all_data(self,model,field_list):
        print("\t%s Tablosu Kayıt Bilgileri Ayrıştırılıyor." % model.__name__)
        wb0 = xlwt.Workbook()
        sht0= wb0.add_sheet(model._meta.db_table)
        for x,field in enumerate(field_list):
            sht0.write(0,x,field.name)
        y=1
        for obj in model.objects.all():
            x=0
            for field in field_list:
                if field.get_internal_type()=="ForeignKey":
                    if getattr(obj,field.name):
                        sht0.write(y,x,str(getattr(obj,field.name).id))
                    else:
                        sht0.write(y,x,"")
                elif field.get_internal_type()=="DateTimeField":
                    if getattr(obj,field.name):
                        sht0.write(y,x,getattr(obj,field.name).strftime("%Y-%m-%d %H-%M-%S"))
                    else:
                        sht0.write(y,x,"")
                elif field.get_internal_type()=="DateField":
                    if getattr(obj,field.name):
                        sht0.write(y,x,getattr(obj,field.name).strftime("%Y-%m-%d"))
                    else:
                        sht0.write(y,x,"")
                elif field.get_internal_type()=="TimeField":
                    if getattr(obj,field.name):
                        sht0.write(y,x,getattr(obj,field.name).strftime("%H-%M-%S"))
                    else:
                        sht0.write(y,x,"")
                else:
                    if getattr(obj,field.name):
                        sht0.write(y,x,str(getattr(obj,field.name)))
                    else:
                        sht0.write(y,x,"")
                x+=1
            y+=1
        wb0.save("data/%s.xls"%(model._meta.db_table))
        print("\t%s Tablosu Kayıt Bilgileri Dışarı Aktarıldı." % model.__name__)

class ToexportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'toexport'
    verbose_name = 'Export Structure To Excel'

    def ready(self):
        pass
        ExportData().code_info()

