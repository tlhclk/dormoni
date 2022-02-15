# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\main\migrations\0006_auto_20211229_1054.py
# Compiled at: 2021-12-29 10:54:58
# Size of source mod 2**32: 4505 bytes
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
     ('schema', '0008_auto_20211229_1054'),
     ('main', '0005_rename_groupmodel_peoplegroupmodel')]
    operations = [
     migrations.AlterField(model_name='corporationmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='departmentmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='peoplegroupmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='schoolmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='taskschedulermodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.CreateModel(name='ReportModel',
       fields=[
      (
       'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Başlık')),
      (
       'group_by_field', models.CharField(blank=True, max_length=50, null=True, verbose_name='Gruplama Alanı')),
      (
       'group_count', models.CharField(blank=True, max_length=50, null=True, verbose_name='Grup Adedi')),
      (
       'text_field', models.CharField(blank=True, max_length=50, null=True, verbose_name='Metin Alanı')),
      (
       'value_field', models.CharField(blank=True, max_length=50, null=True, verbose_name='Değer Alanı')),
      (
       'date_field', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tarih Alanı')),
      (
       'report_type', models.CharField(blank=True, choices=[('1', 'Pie'), ('1', 'Line'), ('1', 'Bar')], max_length=50, null=True, verbose_name='Rapor Tipi')),
      (
       'code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Kodu')),
      (
       'desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
      (
       'app_id', models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.SET_NULL), to='schema.appmodel', verbose_name='Uygulama')),
      (
       'table_id', models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.SET_NULL), to='schema.tablemodel', verbose_name='Tablo'))],
       options={'verbose_name':'Rapor Şemaları', 
      'db_table':'main_report', 
      'ordering':[
       '-app_id', '-table_id']}),
     migrations.CreateModel(name='ReportFilterModel',
       fields=[
      (
       'id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'field_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Alanı')),
      (
       'filter_type', models.CharField(blank=True, choices=[('1', 'e'), ('2', 'gt'), ('3', 'gte'), ('4', 'lt'), ('5', 'lte'), ('6', 'in'), ('7', 'out'), ('8', 'limit'), ('9', 'last_in'), ('10', 'next_in')], max_length=50, null=True, verbose_name='Tipi')),
      (
       'value', models.CharField(blank=True, max_length=50, null=True, verbose_name='Değeri')),
      (
       'date_detail', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tarih Detayı')),
      (
       'report_id', models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.SET_NULL), to='main.reportmodel', verbose_name='Rapor Şeması'))],
       options={'verbose_name':'Rapor Şema Filtreleri', 
      'db_table':'main_reportfilter', 
      'ordering':[
       '-report_id']})]