# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\main\migrations\0009_auto_20211229_1203.py
# Compiled at: 2021-12-29 12:03:43
# Size of source mod 2**32: 1263 bytes
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
     ('schema', '0008_auto_20211229_1054'),
     ('main', '0008_auto_20211229_1156')]
    operations = [
     migrations.AlterField(model_name='reportmodel',
       name='group_by_field',
       field=models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.SET_NULL), related_name='report_group', to='schema.fieldmodel', verbose_name='Gruplama Model Alanı')),
     migrations.AlterField(model_name='reportmodel',
       name='text_field',
       field=models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.SET_NULL), related_name='report_text', to='schema.fieldmodel', verbose_name='Metin Model Alanı')),
     migrations.AlterField(model_name='reportmodel',
       name='value_field',
       field=models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.SET_NULL), related_name='report_value', to='schema.fieldmodel', verbose_name='Değer Model Alanı'))]