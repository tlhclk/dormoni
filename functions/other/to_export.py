# -*- coding: utf-8 -*-
from hashlib import new
from xmlrpc.client import boolean
from django.apps import AppConfig, apps
from django.urls import *
from django.conf import settings
import xlwt, inspect, types, builtins, os


class ExportData:
    app_data = True
    table_data = True
    field_data = True


    def app_init(self):
        self.app_model = apps.get_model('schema', 'AppModel')
        print('\tUygulama Bilgileri Ayrıştırılıyor.')
        config_list = apps.get_app_configs()
        for config in config_list:
            app_list=self.app_model.objects.filter(label=config.label)
            if len(app_list)>0:
                new_app=app_list[0]
            else:
                new_app = self.app_model()
            #label
            new_app.label = config.label
            #name
            new_app.name = config.name
            #type_id
            if 'django' in config.name:
                new_app.type_id_id=2
            else:
                new_app.type_id_id=1
            #verbose_name
            new_app.verbose_name = config.verbose_name
            new_app.save()
            print('\t\t%s Uygulaması Kaydedildi.' %(new_app.verbose_name))
            #App Models
            if self.table_data:
                self.table_init(config,new_app)
        print('\tUygulama Bilgileri Kaydedildi.')

    def table_init(self,app_obj,app_id):
        self.table_model = apps.get_model('schema', 'TableModel')
        print('\t\t\tTablo Bilgileri Ayrıştırılıyor.')
        for tk,tm in app_obj.models.items():
            table_queryset = self.table_model.objects.filter(db_table=tm._meta.db_table)
            ft=False
            if len(table_queryset)>0:
                new_table=table_queryset[0]
            else:
                new_table=self.table_model()
                ft=True
            #app_id
            new_table.app_id_id=app_id.id
            #order
            new_table.order=len(self.table_model.objects.filter(app_id_id=app_id.id))+1
            #name
            new_table.name=tm.__name__
            #db_table
            new_table.db_table=tm._meta.db_table
            #verbose_name
            new_table.verbose_name=tm._meta.verbose_name
            #list_title
            new_table.list_title='%s Listesi' % (tm._meta.verbose_name)
            #form_title
            new_table.form_title='%s Formu' % (tm._meta.verbose_name)
            #detail_title
            new_table.detail_title='%s Detayı' % (tm._meta.verbose_name)
            #ordering
            new_table.ordering=tm._meta.ordering
            new_table.save()
            print('\t\t\t\t%s Tablosu Kaydedildi.' %(new_table.verbose_name))
            #Model Fields
            if self.field_data:
                self.field_init(tm._meta.fields,new_table)
            self.path_init(new_table)
            self.permission_init(new_table)
        print('\t\t\tTablo Bilgileri Kaydedildi.')

    def field_init(self,field_list,table_id):
        self.field_model = apps.get_model('schema', 'FieldModel')
        print('\t\t\t\t\tTablo Bilgileri Ayrıştırılıyor.')
        for field in field_list:
            field_queryset=self.field_model.objects.filter(table_id=table_id).filter(name=field.name)
            if len(field_queryset)>0:
                new_field=field_queryset[0]
            else:
                new_field=self.field_model()
            #table_id
            new_field.table_id=table_id
            #order
            new_field.order=len(self.field_model.objects.filter(table_id=table_id))+1
            #name
            new_field.name=field.name
            #verbose_name
            new_field.verbose_name=field.verbose_name
            #field
            new_field.field=field.get_internal_type()
            #null
            new_field.null=field.null
            #blank
            new_field.blank=field.blank
            #max_length
            new_field.max_length=field.max_length
            if new_field.field == "ForeignKey":
                #on_delete
                new_field.on_delete="models.SET_NULL"
                #related_name
                new_field.related_name=table_id.name.lower().replace("model","")+"_info"
                #to
                new_field.to=field.remote_field.model.__name__
            #default
            try:
                if len(field.defalut())==0:
                    pass
                else:
                    new_field.default=str(field.default())
            except :
                new_field.default=str(field.default)
            #max_digits
            if hasattr(field,'max_digits'):
                new_field.max_digits=field.max_digits
            else:
                new_field.max_digits=''
            #decimal_places
            if hasattr(field,'decimal_places'):
                new_field.decimal_places=field.decimal_places
            else:
                new_field.decimal_places=''
            #is_generated
            new_field.is_generated='False'
            #show_list
            new_field.show_list='True'
            #show_detail
            new_field.show_list='True'
            #form_create
            new_field.show_list='True'
            #form_update
            new_field.show_list='True'
            #form_delete
            new_field.show_list='True'
            #help_text
            new_field.help_text=field.help_text
            #error_messages
            new_field.error_messages=field.error_messages
            new_field.save()
            print('\t\t\t\t\t\t%s Tablo Alanı Kaydedildi.' %(new_field.verbose_name))
        print('\t\t\t\t\tTablo Bilgileri Kaydedildi.')
    
    def path_init(self,table_id):
        self.path_model = apps.get_model('schema', 'PathModel')
        print('\t\t\t\t\tGüzergah Bilgileri Ayrıştırılıyor.')
        if len(self.path_model.objects.filter(code="%02d-%03d-c" % (table_id.app_id.id,table_id.id)))==0:# create
            npc=self.path_model()
            npc.app_id=table_id.app_id
            npc.type_id_id=9
            npc.title="Yeni %s" % (table_id.form_title)
            npc.path="/global_view/create/"
            npc.name="crete_%s" % (table_id.name.lower().replace("model",""))
            npc.code="%02d-%03d-c" % (table_id.app_id.id,table_id.id)
            npc.action="Create"
            npc.icon_code="fa-regular fa-square-plus"
            npc.save()
        if len(self.path_model.objects.filter(code="%02d-%03d-u" % (table_id.app_id.id,table_id.id)))==0:# update
            npu=self.path_model()
            npu.app_id=table_id.app_id
            npu.type_id_id=12
            npu.title="Düzenleme %s" % (table_id.form_title)
            npu.path="/global_view/update/%s/" % (table_id.name)
            npu.name="update_%s" % (table_id.name.lower().replace("model",""))
            npu.code="%02d-%03d-u" % (table_id.app_id.id,table_id.id)
            npu.action="Update"
            npu.icon_code="fa-regular fa-square-pen"
            npu.save()
        if len(self.path_model.objects.filter(code="%02d-%03d-d" % (table_id.app_id.id,table_id.id)))==0:# delete
            npd=self.path_model()
            npd.app_id=table_id.app_id
            npu.type_id_id=13
            npd.title="Silme %s" % (table_id.form_title)
            npd.path="/global_view/delete/%s/" % (table_id.name)
            npd.name="delete_%s" % (table_id.name.lower().replace("model",""))
            npd.code="%02d-%03d-d" % (table_id.app_id.id,table_id.id)
            npd.action="Delete"
            npd.icon_code="fa-regular fa-square-minus"
            npd.save()
        if len(self.path_model.objects.filter(code="%02d-%03d-l" % (table_id.app_id.id,table_id.id)))==0:# list
            npl=self.path_model()
            npl.app_id=table_id.app_id
            npl.type_id_id=10
            npl.title="%s" % (table_id.list_title)
            npl.path="/global_view/list/"
            npl.name="list_%s" % (table_id.name.lower().replace("model",""))
            npl.code="%02d-%03d-l" % (table_id.app_id.id,table_id.id)
            npl.action="List"
            npl.icon_code="fa-regular fa-square-list"
            npl.save()
        if len(self.path_model.objects.filter(code="%02d-%03d-t" % (table_id.app_id.id,table_id.id)))==0:# detail
            npt=self.path_model()
            npt.app_id=table_id.app_id
            npt.type_id_id=11
            npt.title="%s" % (table_id.detail_title)
            npt.path="/global_view/detail/%s/" % (table_id.name)
            npt.name="detail_%s" % (table_id.name.lower().replace("model",""))
            npt.code="%02d-%03d-t" % (table_id.app_id.id,table_id.id)
            npt.action="Detail"
            npt.icon_code="fa-regular fa-square-info"
            npt.save()
        print('\t\t\t\t\tGüzergah Bilgileri Kaydedildi.')

    def ready(self):
        print('Dışarı Aktarma İşlemi Başladı.')
        if self.app_data:
            self.app_init()
        print('Dışarı Aktarma işlemi Bitti.')



