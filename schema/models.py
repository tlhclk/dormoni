# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.hashers import make_password
from datetime import date
from django.contrib.auth.models import User
from functions.db.manager import CustomManager

# -*- coding: utf-8 -*-
from django.db import models
from parameters.models import AppTypeModel, PathTypeModel

class AppModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    label = models.CharField(verbose_name='Etiket', null=True, blank=True, max_length=50)
    type_id = models.ForeignKey(verbose_name='Uygulama Türü', null=True, blank=True, on_delete=(models.SET_NULL), to=AppTypeModel)
    verbose_name = models.CharField(verbose_name='Başlık', null=True, blank=True, max_length=100)
    sidebar_icon = models.CharField(verbose_name='İcon', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'schema_app'
        ordering = ['name']
        verbose_name = 'Uygulama'

    def __str__(self):
        return '%s' % self.verbose_name


class TableModel(models.Model):
    app_id = models.ForeignKey(verbose_name='Uygulama', null=True, blank=True, on_delete=(models.SET_NULL), to=AppModel)
    order = models.IntegerField(verbose_name='Sıra No', null=True, blank=True)
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    db_table = models.CharField(verbose_name='Veritabanı Tablo Adı', null=True, blank=True, max_length=50)
    verbose_name = models.CharField(verbose_name='Başlık', null=True, blank=True, max_length=100)
    list_title = models.CharField(verbose_name='Liste Başlığı', null=True, blank=True, max_length=200)
    form_title = models.CharField(verbose_name='Form Başlığı', null=True, blank=True, max_length=50)
    detail_title = models.CharField(verbose_name='Detay Başlığı', null=True, blank=True, max_length=50)
    ordering = models.CharField(verbose_name='Sıralama', null=True, blank=True, max_length=100)
    verbose_name_plural = models.CharField(verbose_name='Çoğul Başlık', null=True, blank=True, max_length=100)
    sidebar_icon = models.CharField(verbose_name='İcon', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'schema_table'
        ordering = ['app_id', 'order']
        verbose_name = 'Tablo'

    def __str__(self):
        return '%s > %s' % (self.app_id, self.verbose_name)


class FieldModel(models.Model):
    table_id = models.ForeignKey(verbose_name='Model Adı', null=True, blank=True, on_delete=(models.SET_NULL), to=TableModel)
    order = models.IntegerField(verbose_name='Sıra No', null=True, blank=True)
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    verbose_name = models.CharField(verbose_name='Başlık', null=True, blank=True, max_length=100)
    field = models.CharField(verbose_name='Alan Türü', null=True, blank=True, max_length=100)
    null = models.BooleanField(verbose_name='Null ?', null=True, blank=True, default=True)
    blank = models.BooleanField(verbose_name='Blank ?', null=True, blank=True, default=True)
    max_length = models.CharField(verbose_name='En Fazla Uzunluk', null=True, blank=True, max_length=5)
    on_delete = models.CharField(verbose_name='Silinme Şekli', null=True, blank=True, max_length=100)
    related_name = models.CharField(verbose_name='İlişki Adı', null=True, blank=True, max_length=100)
    to = models.CharField(verbose_name='İlişkili Tablo', null=True, blank=True, max_length=50)
    default = models.CharField(verbose_name='Varsayılan Değer', null=True, blank=True, max_length=100)
    max_digits = models.CharField(verbose_name='En Fazla Hane', null=True, blank=True, max_length=5)
    decimal_places = models.CharField(verbose_name='Virgülden Sonraki Hane', null=True, blank=True, max_length=5)
    is_generated = models.BooleanField(verbose_name='Oluşturulan', default=False, null=True, blank=True)
    show_list = models.BooleanField(verbose_name='Listede Gösterimi', default=True, null=True, blank=True)
    form_create = models.BooleanField(verbose_name='Oluşturulabilir', default=True, null=True, blank=True)
    show_detail = models.BooleanField(verbose_name='Detayda Gösterimi', default=True, null=True, blank=True)
    form_update = models.BooleanField(verbose_name='Değiştirilebilir', default=True, null=True, blank=True)
    form_delete = models.BooleanField(verbose_name='Silinebilir', default=True)
    help_text = models.CharField(verbose_name='Yardımcı Metin', null=True, blank=True, max_length=500)
    error_messages = models.CharField(verbose_name='Hata Mesajları', null=True, blank=True, max_length=500)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'schema_field'
        ordering = ['table_id', 'order']
        verbose_name = 'Model Alanı'

    def __str__(self):
        return '%s > %s' % (self.table_id.verbose_name, self.verbose_name)


class PathModel(models.Model):
    app_id = models.ForeignKey(verbose_name='Uygulama', null=True, blank=True, on_delete=(models.SET_NULL), to=AppModel)
    type_id = models.ForeignKey(verbose_name='Güzergah Tipi', null=True, blank=True, on_delete=(models.SET_NULL), to=PathTypeModel)
    title = models.CharField(verbose_name='Başlık',null=True,blank=True,max_length=100)
    path = models.CharField(verbose_name='Güzergah',null=True,blank=True,max_length=200)
    name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
    code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=100)
    action = models.CharField(verbose_name='Eylemi',null=True,blank=True,max_length=100)
    icon_code = models.CharField(verbose_name='Sidebar İcon Kodu', null=True, blank=True, max_length=100)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=100)
    objects = CustomManager()

    class Meta:
        db_table = 'schema_path'
        ordering = ['name']
        verbose_name = 'Güzergah'

    def __str__(self):
        return '%s' % (self.title)
    

class ParentPathModel(models.Model):
    path_id = models.ForeignKey(verbose_name='Güzergah', on_delete=(models.CASCADE), to=PathModel,default="",related_name="parentpath_info")
    menu_level = models.CharField(verbose_name='Menü Seviyesi',null=True,blank=True,max_length=100)
    order = models.CharField(verbose_name='Sıra No',null=True,blank=True,max_length=10)
    desc = models.CharField(verbose_name='Açıklama',null=True,blank=True,max_length=200)
    
    class Meta:
        db_table = 'schema_parentpath'
        ordering = ['order']
        verbose_name = 'Üst Menü Güzergah'

    def __str__(self):
        return '%s' % (str(self.path_id))

class ChildPath(models.Model):
    parentpath_id = models.ForeignKey(verbose_name='Güzergah', on_delete=(models.CASCADE), to=ParentPathModel,default="",related_name="childpath_info")
    path_id = models.ForeignKey(verbose_name='Güzergah', on_delete=(models.CASCADE), to=PathModel,default="",related_name="childpath_info")
    menu_level = models.CharField(verbose_name='Menü Seviyesi',null=True,blank=True,max_length=100)
    order = models.CharField(verbose_name='Sıra No',null=True,blank=True,max_length=10)
    desc = models.CharField(verbose_name='Açıklama',null=True,blank=True,max_length=200)
    
    class Meta:
        db_table = 'schema_childpath'
        ordering = ['order','parentpath_id']
        verbose_name = 'Alt Menü Güzergah'

    def __str__(self):
        return '%s > %s' % (str(self.parentpath_id),str(self.path_id))
