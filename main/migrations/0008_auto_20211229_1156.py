# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\main\migrations\0008_auto_20211229_1156.py
# Compiled at: 2021-12-29 11:56:24
# Size of source mod 2**32: 940 bytes
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
     ('schema', '0008_auto_20211229_1054'),
     ('main', '0007_auto_20211229_1100')]
    operations = [
     migrations.RemoveField(model_name='reportfiltermodel',
       name='field_name'),
     migrations.AddField(model_name='reportfiltermodel',
       name='field_id',
       field=models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.SET_NULL), to='schema.fieldmodel', verbose_name='Model Alanı')),
     migrations.AlterField(model_name='reportfiltermodel',
       name='value',
       field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Değeri'))]