# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\main\models.py
# Compiled at: 2021-12-31 12:13:13
# Size of source mod 2**32: 8397 bytes
from django.db import models
from django.db.models.fields import related
from parameters.models import CountryModel, MarketModel, CorporationTypeModel, CityModel, TownModel, SchoolTypeModel, PeriodModel
from schema.models import AppModel, TableModel, FieldModel
from datetime import datetime

class DepartmentModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'main_department'
        ordering = ['name']
        verbose_name = 'Bölüm'

    def __str__(self):
        return '%s' % self.name


class CorporationModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    market_id = models.ForeignKey(verbose_name='Market Tipi', null=True, blank=True, on_delete=(models.SET_NULL), to=MarketModel)
    type_id = models.ForeignKey(verbose_name='Firma Tipi', null=True, blank=True, on_delete=(models.SET_NULL), to=CorporationTypeModel)
    city_id = models.ForeignKey(verbose_name='İli', null=True, blank=True, on_delete=(models.SET_NULL), to=CityModel)
    town_id = models.ForeignKey(verbose_name='İlçesi', null=True, blank=True, on_delete=(models.SET_NULL), to=TownModel)
    hyperlink = models.CharField(verbose_name='Bağlantı Adresi', null=True, blank=True, max_length=200)
    address = models.CharField(verbose_name='Adresi', null=True, blank=True, max_length=200)
    phone_number = models.CharField(verbose_name='Telefon Numarası', null=True, blank=True, max_length=20)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'main_corporation'
        ordering = ['name']
        verbose_name = 'Firma'

    def __str__(self):
        return '%s' % self.name


class PeopleGroupModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'main_group'
        ordering = ['name']
        verbose_name = 'Rehber Grubu'

    def __str__(self):
        return '%s' % self.name


class SchoolModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    type_id = models.ForeignKey(verbose_name='Okul Tipi', null=True, blank=True, on_delete=(models.SET_NULL), to=SchoolTypeModel)
    city_id = models.ForeignKey(verbose_name='İli', null=True, blank=True, on_delete=(models.SET_NULL), to=CityModel)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'main_school'
        ordering = ['city_id', 'name']
        verbose_name = 'Okul'

    def __str__(self):
        return '%s > %s' % (self.city_id, self.name)


class TaskSchedulerModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    period_id = models.ForeignKey(verbose_name='Period Sıklığı', null=True, blank=True, on_delete=(models.SET_NULL), to=PeriodModel)
    period_amount = models.CharField(verbose_name='Period Miktarı', null=True, blank=True, max_length=10)
    run_time = models.DateTimeField(verbose_name='Çalıştırma Zamanı', null=True, blank=True)
    run_func = models.CharField(verbose_name='Çalıştırılacak Fonksiyon', null=True, blank=True, max_length=200)
    is_active = models.BooleanField(verbose_name='Aktif Mi?', null=True, blank=True, default=0)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'main_taskscheduler'
        ordering = ['-is_active', '-run_time']
        verbose_name = 'Görev Zamanlayıcısı'

    def __str__(self):
        return '[%s] %s' % (self.last_date.strftime('%Y-%m-%d'), self.name)


class ReportModel(models.Model):
    title = models.CharField(verbose_name='Başlık', null=True, blank=True, max_length=200)
    app_id = models.ForeignKey(verbose_name='Uygulama', null=True, blank=True, on_delete=(models.SET_NULL), to=AppModel)
    table_id = models.ForeignKey(verbose_name='Tablo', null=True, blank=True, on_delete=(models.SET_NULL), to=TableModel)
    group_by_field_id = models.ForeignKey(verbose_name='Gruplama Model Alanı', null=True, blank=True, on_delete=(models.SET_NULL), to=FieldModel, related_name='report_group')
    group_count = models.CharField(verbose_name='Grup Adedi', null=True, blank=True, max_length=50)
    text_field_id = models.ForeignKey(verbose_name='Metin Model Alanı', null=True, blank=True, on_delete=(models.SET_NULL), to=FieldModel, related_name='report_text')
    value_field_id = models.ForeignKey(verbose_name='Değer Model Alanı', null=True, blank=True, on_delete=(models.SET_NULL), to=FieldModel, related_name='report_value')
    date_field_id = models.ForeignKey(verbose_name='Tarih Model Alanı', null=True, blank=True, on_delete=(models.SET_NULL), to=FieldModel, related_name='report_date')
    report_type = models.CharField(verbose_name='Rapor Tipi', null=True, blank=True, max_length=50, choices=[('1', 'Pie'), ('2', 'Line'), ('3', 'Bar')])
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=200)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'main_report'
        ordering = ['-app_id', '-table_id']
        verbose_name = 'Rapor Şemaları'

    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        error_dict = {}
        if self.group_by_field_id:
            if self.group_by_field_id.field not in ('CharField', 'ForeignKey', 'BooleanField'):
                error_dict['group_by_field_id'] = self.group_by_field_id.field
            if self.group_by_field_id.table_id == self.table_id:
                error_dict['group_by_field_id__table_id'] = self.group_by_field_id.table_id
        if self.text_field_id:
            if self.text_field_id.field not in ('CharField', 'ForeignKey', 'BooleanField',
                                                'DateField', 'DateTimeField', 'TimeField'):
                error_dict['text_field_id'] = self.text_field_id.field
            if self.text_field_id.table_id == self.table_id:
                error_dict['text_field_id__table_id'] = self.text_field_id.table_id
        if self.value_field_id:
            if self.value_field_id.field not in ('IntegerField', 'DecimalField'):
                error_dict['value_field_id'] = self.value_field_id.field
            if self.value_field_id.table_id == self.table_id:
                error_dict['value_field_id__table_id'] = self.value_field_id.table_id
        if self.date_field_id:
            if self.date_field_id.field not in ('DateField', 'TimeField', 'DateTimeField'):
                error_dict['date_field_id'] = self.date_field_id.field
            if self.date_field_id.table_id == self.table_id:
                error_dict['date_field_id__table_id'] = self.date_field_id.table_id
        elif len(error_dict) > 0:
            print(error_dict)
        else:
            return (super().save)(*args, **kwargs)


class ReportFilterModel(models.Model):
    report_id = models.ForeignKey(verbose_name='Rapor Şeması', null=True, blank=True, on_delete=(models.SET_NULL), to=ReportModel)
    field_id = models.ForeignKey(verbose_name='Model Alanı', null=True, blank=True, on_delete=(models.SET_NULL), to=FieldModel)
    filter_type = models.CharField(verbose_name='Tipi', null=True, blank=True, max_length=50, choices=[('1', 'e'), ('2', 'ne'), ('3', 'gt'), ('4', 'gte'), ('5', 'lt'), ('6', 'lte'), ('7', 'in'), ('8', 'out'), ('9', 'limit'), ('10', 'last_in'), ('11', 'next_in'), ('12', 'order_by')])
    value = models.CharField(verbose_name='Değeri', null=True, blank=True, max_length=100)
    date_detail = models.CharField(verbose_name='Tarih Detayı', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'main_reportfilter'
        ordering = ['-report_id']
        verbose_name = 'Rapor Şema Filtreleri'

    def __str__(self):
        return '%s > %s=[%s]=%s' % (self.report_id, self.field_id, self.filter_type, self.value)

    def save(self, *args, **kwargs):
        error_dict = {}
        if self.field_id:
            if self.report_id:
                if self.field_id.table_id != self.report_id.table_id:
                    error_dict['field_id__table_id'] = self.field_id.table_id
            else:
                error_dict['report_id'] = 'None'
        elif len(error_dict) > 0:
            print(error_dict)
        else:
            return (super().save)(*args, **kwargs)