# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\schema\models.py
# Compiled at: 2021-12-30 11:24:02
# Size of source mod 2**32: 6973 bytes
from django.db import models
from parameters.models import AppTypeModel, PathTypeModel, FunctionTypeModel

class AppModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
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
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    db_table = models.CharField(verbose_name='Veritabanı Tablo Adı', null=True, blank=True, max_length=50)
    verbose_name = models.CharField(verbose_name='Başlık', null=True, blank=True, max_length=100)
    list_title = models.CharField(verbose_name='Liste Başlığı', null=True, blank=True, max_length=200)
    form_title = models.CharField(verbose_name='Form Başlığı', null=True, blank=True, max_length=50)
    detail_title = models.CharField(verbose_name='Detay Başlığı', null=True, blank=True, max_length=50)
    app_id = models.ForeignKey(verbose_name='Uygulama', null=True, blank=True, on_delete=(models.SET_NULL), to=AppModel)
    ordering = models.CharField(verbose_name='Sıralama', null=True, blank=True, max_length=100)
    order = models.IntegerField(verbose_name='Sıra No', null=True, blank=True)
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
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    verbose_name = models.CharField(verbose_name='Başlık', null=True, blank=True, max_length=100)
    field = models.CharField(verbose_name='Alan Türü', null=True, blank=True, max_length=100)
    table_id = models.ForeignKey(verbose_name='Model Adı', null=True, blank=True, on_delete=(models.SET_NULL), to=TableModel)
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
    order = models.IntegerField(verbose_name='Sıra No', null=True, blank=True)
    help_text = models.CharField(verbose_name='Yardımcı Metin', null=True, blank=True, max_length=500)
    error_messages = models.CharField(verbose_name='Hata Mesajları', null=True, blank=True, max_length=500)
    auto_now = models.CharField(verbose_name='Otomatik Zaman Ekle', null=True, blank=True, max_length=5)
    auto_now_add = models.CharField(verbose_name='Otomatik Zamanı Düzenle', null=True, blank=True, max_length=5)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'schema_field'
        ordering = ['table_id', 'order']
        verbose_name = 'Model Alanı'

    def __str__(self):
        return '%s > %s' % (self.table_id.verbose_name, self.verbose_name)


class PathModel(models.Model):
    title = models.CharField(verbose_name='Başlık', null=True, blank=True, max_length=100)
    path = models.CharField(verbose_name='Güzergah', null=True, blank=True, max_length=100)
    view_func = models.CharField(verbose_name='View Fonksiyonu', null=True, blank=True, max_length=100)
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    app_id = models.ForeignKey(verbose_name='Uygulama', null=True, blank=True, on_delete=(models.SET_NULL), to=AppModel)
    type_id = models.ForeignKey(verbose_name='Güzergah Tipi', null=True, blank=True, on_delete=(models.SET_NULL), to=PathTypeModel)
    location = models.CharField(verbose_name='Konumu', null=True, blank=True, max_length=100)
    icon_code = models.CharField(verbose_name='Sidebar İcon Kodu', null=True, blank=True, max_length=100)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'schema_path'
        ordering = ['app_id', 'name']
        verbose_name = 'Güzergah Listesi'

    def __str__(self):
        return '%s >%s' % (self.app_id, self.title)


class FunctionModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    app_id = models.ForeignKey(verbose_name='Uygulama', null=True, blank=True, on_delete=(models.SET_NULL), to=AppModel)
    file_path = models.CharField(verbose_name='Dosya Adı', null=True, blank=True, max_length=500)
    parent = models.CharField(verbose_name='Üst Fonskiyon', null=True, blank=True, max_length=10)
    order = models.CharField(verbose_name='Sırası', null=True, blank=True, max_length=10)
    type_id = models.ForeignKey(verbose_name='Fonksiyon Türü', null=True, blank=True, on_delete=(models.SET_NULL), to=FunctionTypeModel)
    data_path = models.CharField(verbose_name='Veri Konumu', null=True, blank=True, max_length=500)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'schema_function'
        ordering = []
        verbose_name = 'Fonksiyon'

    def __str__(self):
        return '%s > %s' % (self.app_id, self.name)