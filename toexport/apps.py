from django.apps import AppConfig, apps
from django.urls import *
from django.conf import settings
import xlwt,inspect, types,builtins,os


class ExportData:
    # settings
    app_data = True
    table_data = True
    field_data = True
    def __init__(self):
        if self.app_data:
            self.app_init()
            if self.table_data:
                self.table_init()
                if self.field_data:
                    self.field_init()
        if os.path.exists(os.getcwd()+"/data"):
            if not os.path.isdir(os.getcwd()+"/data"):
                os.mkdir(os.getcwd()+"/data")
        else:
            os.mkdir(os.getcwd()+"/data")
    
    def app_init(self):
        self.app_model=apps.get_model("schema","AppModel")
        self.new_app_data={}
        self.app_wb=xlwt.Workbook()
        self.app_wb_name="schema_app.xls"
        self.shta=self.app_wb.add_sheet("schema_app")
        self.ax,self.ay=0,1
        app_header=["#","name","type_id","verbose_name"]
        for title in app_header:
            self.shta.write(0,self.ax,title)
            self.ax+=1
    
    def table_init(self):
        self.table_model=apps.get_model("schema","TableModel")
        self.new_table_data={}
        self.table_wb=xlwt.Workbook()
        self.table_wb_name="schema_table.xls"
        self.shtt=self.table_wb.add_sheet("schema_table")
        self.tx,self.ty=0,1
        table_header=["#","name","db_table","verbose_name","list_title","form_title","detail_title","ordering","order","verbose_name_plural","app_id"]
        for title in table_header:
            self.shtt.write(0,self.tx,title)
            self.tx+=1

    def field_init(self):
        self.field_model=apps.get_model("schema","FieldModel")
        self.new_field_data={}
        self.field_wb=xlwt.Workbook()
        self.field_wb_name="schema_field.xls"
        self.shtf=self.field_wb.add_sheet("schema_field")
        self.fx,self.fy=0,1
        key_list=["#","name","verbose_name","field","null","blank","max_length","on_delete","to","default",
                    "max_digits","decimal_places","is_generated","show_list","form_create","show_detail","form_update",
                    "form_delete","order","help_text","error_messages","auto_now","auto_now_add","table_id"]
        for key in key_list:
            self.shtf.write(0,self.fx,key)
            self.fx+=1

    def close(self):
        if self.app_data:
            self.app_wb.save("data/"+self.app_wb_name)
            if self.table_data:
                self.table_wb.save("data/"+self.table_wb_name)
                if self.field_data:
                    self.field_wb.save("data/"+self.field_wb_name)
    
    def get_app(self,app_name):
        app_list=self.app_model.objects.filter(name=app_name)

        if len(app_list)==1:
            return app_list[0]
        else:
            return None
    
    def get_table(self,table_name):
        table_list=self.table_model.objects.filter(name=table_name)
        if len(table_list)==1:
            return table_list[0]
        else:
            return None
    
    def get_field(self,table_obj,field_name):
        field_list=self.field_model.objects.filter(table_id=table_obj).filter(name=field_name)
        if len(field_list)==1:
            return field_list[0]
        else:
            return None

    def get_app_info(self):
        print("\tUygulama Bilgileri Ayrıştırılıyor.")
        config_list=apps.get_app_configs()
        root_path=os.getcwd()
        folder_list=[f for f in os.listdir(root_path) if not os.path.isfile(os.path.join(root_path, f))]
        project_name = settings.ROOT_URLCONF.split(".")[0]
        for config in config_list:
            new_app=self.app_model()
            # verbose_nmae
            if hasattr(config,"verbose_name"):
                new_app.verbose_name=str(config.verbose_name)
            else:
                new_app.verbose_name=""
            self.shta.write(self.ay,3,new_app.verbose_name)
            # app_type
            if config.name == project_name:
                new_app.type_id_id=2

            elif config.name in folder_list:
                app_path=os.path.join(root_path, config.name)
                folder_list2=[f for f in os.listdir(app_path) if os.path.isfile(os.path.join(app_path, f))]
                type_list=[f.split(".")[-1] for f in folder_list2]
                if "apps.py" in folder_list2 and "models.py" in folder_list2:
                    new_app.type_id_id=1
                elif "py" in type_list:
                    new_app.type_id_id=5
                else:
                    new_app.type_id_id=3
            else:
                new_app.type_id_id=4
            self.shta.write(self.ay,2,new_app.type_id_id)
            # name
            self.shta.write(self.ay,1,config.name)
            new_app.name=config.name
            # id
            app_obj=self.get_app(config.name)
            if app_obj:
                self.shta.write(self.ay,0,app_obj.id)
            else:
                new_app.save()
                self.shta.write(self.ay,0,new_app.id)
            
            self.ay+=1
        print("\tUygulama Bilgileri Dışarı Aktarıldı.")

    def get_table_info(self):
        print("\tTablo Bilgileri Ayrıştırılıyor.")
        all_models = apps.get_models()
        self.field_dict={}
        for model_data in  all_models:
            field_list=[]
            new_table=self.table_model()
            try:
                value5 = model_data.__name__
                table_obj=self.get_table(value5)
                if table_obj:
                    new_table=table_obj
                # str_func as note
                value2 = inspect.getsource(model_data.__str__).strip().replace("\n","\\n").replace("    ","\\t")
                self.shtt.write(self.ty,11,str(value2))
                # db_table
                value3 = model_data._meta.db_table
                new_table.db_table=value3
                self.shtt.write(self.ty,2,str(value3))
                # ordering
                value4 = model_data._meta.ordering
                new_table.ordering=value4
                self.shtt.write(self.ty,7,str(value4))
                # name
                new_table.name=value5
                self.shtt.write(self.ty,1,str(value5))
                # verbose_name
                value6 = model_data._meta.verbose_name
                new_table.verbose_name=value6
                self.shtt.write(self.ty,3,str(value6))
                # app__name
                value7 = ".".join(model_data.__module__.split(".")[:-1])
                # app_id
                app_obj=self.get_app(value7)
                if app_obj:
                    new_table.app_id=app_obj
                    self.shtt.write(self.ty,10,str(app_obj.id))
                else:
                    self.shtt.write(self.ty,10,"")
                # model_alanları
                field_list=model_data._meta.fields
                # list_title
                value8 = "%s Listesi" % model_data._meta.verbose_name
                if not new_table.list_title:
                    new_table.list_title=value8
                self.shtt.write(self.ty,4,str(value8))
                # form_title
                value9 = "%s"+" %s Formu" % model_data._meta.verbose_name
                if not new_table.form_title:
                    new_table.form_title=value9
                self.shtt.write(self.ty,5,str(value9))
                # detail_title
                value10 = "%s"+" %s Detayı" % model_data._meta.verbose_name
                if not new_table.detail_title:
                    new_table.detail_title=value10
                self.shtt.write(self.ty,6,str(value10))
                # id
                new_table.save()
                self.shtt.write(self.ty,0,new_table.id)
                self.ty+=1
                if self.field_data and app_obj.type_id_id==1:
                    self.get_field_info(new_table,field_list)
            except AttributeError:
                pass
        print("\tTablo Bilgileri Dışarı Aktarıldı.")

    def get_field_info(self,table_obj,field_list):
        print("\t\t%s Tablosu Alan Bilgileri Ayrıştırılıyor." % table_obj.name)
        model_dict={}
        for field in field_list:
            if field.name=="id":
                continue
            #name
            value1=field.name
            field_obj=self.get_field(table_obj,value1)
            if field_obj:
                new_field=field_obj
            else:
                print(str(table_obj),str(field))
                new_field=self.field_model()
            new_field.name=value1
            self.shtf.write(self.fy,1,value1)
            # verbose_name
            value2=str(field.verbose_name)
            new_field.verbose_name=value2
            self.shtf.write(self.fy,2,value2)
            # field
            value3=field.get_internal_type()
            new_field.field=value3
            self.shtf.write(self.fy,3,value3)
            # table__name
            if table_obj:
                new_field.table_id=table_obj
                self.shtf.write(self.fy,23,table_obj.id)
            # null
            value5=field.null
            new_field.null=value5
            self.shtf.write(self.fy,4,value5)
            # blank
            value6=field.blank
            new_field.blank=value6
            self.shtf.write(self.fy,5,value6)
            # max_length
            value7=field.max_length
            new_field.max_length=value7
            self.shtf.write(self.fy,6,value7)
            # to_table
            if field.get_internal_type()=="ForeignKey":
                value9=field.remote_field.model.__name__
                new_field.to=value9
                self.shtf.write(self.fy,8,value9)
                # on_delete
                value8="models.SET_NULL"
                new_field.on_delete=value8
                self.shtf.write(self.fy,7,value8)
            # default
            if type(field.default)==bool:
                value10=str(field.default)
            elif type(field.default)==types.FunctionType:
                value10=str(field.default())
            elif type(field.default)==types.BuiltinMethodType:
                value10=str(field.default())
            else:
                value10=""
            new_field.default=value10
            self.shtf.write(self.fy,9,value10)
            # max_digits & decimal_places
            try:
                value11=field.max_digits
                new_field.max_digits=value11
                self.shtf.write(self.fy,10,value11)
                value12=field.decimal_places
                new_field.decimal_places=value12
                self.shtf.write(self.fy,11,value12)
            except AttributeError:
                pass
            # is_generated
            self.shtf.write(self.fy,12,new_field.is_generated)
            # show_list
            self.shtf.write(self.fy,13,new_field.show_list)
            # form_create
            self.shtf.write(self.fy,14,new_field.form_create)
            # show_deltail
            self.shtf.write(self.fy,15,new_field.show_detail)
            # form_update
            self.shtf.write(self.fy,16,new_field.form_update)
            # form_delete
            self.shtf.write(self.fy,17,new_field.form_delete)
            # order
            if table_obj.name in model_dict:
                model_dict[table_obj.name]+=1
            else:
                model_dict[table_obj.name]=1
            value19=model_dict[table_obj.name]
            if not new_field.order:
                new_field.order=value19
            else:
                value19=new_field.order
            self.shtf.write(self.fy,18,value19)
            # help_text
            #value22=str(field.help_text)
            value22="Done"
            new_field.help_text=value22
            self.shtf.write(self.fy,19,value22)
            # error_messages
            value23=str(field.error_messages)
            new_field.error_messages=value23
            self.shtf.write(self.fy,20,value23)
            # auto_Now
            if hasattr(field,"auto_now"):
                value24=str(field.auto_now)
                new_field.auto_now=value24
                self.shtf.write(self.fy,21,value24)
            # auto_now_add
            if hasattr(field,"auto_now_add"):
                value25=str(field.auto_now_add)
                new_field.auto_now_add=value25
                self.shtf.write(self.fy,22,value25)
            # id
            new_field.save()
            self.shtf.write(self.fy,0,new_field.id)
            self.fy+=1
        print("\t\t%s Tablosu Alan Bilgileri Dışarı Aktarıldı." % field_list[0].model.__name__)





    
    def ready(self):
        print("Dışarı Aktarma İşlemi Başladı.")
        if self.app_data:
            self.get_app_info()
        if self.table_data:
            self.get_table_info()
        self.close()
        print("Dışarı Aktarma işlemi Bitti.")


class ToexportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'toexport'
    verbose_name = 'Export Structure To Excel'

    def ready(self):
        pass
        #ExportData().ready()

