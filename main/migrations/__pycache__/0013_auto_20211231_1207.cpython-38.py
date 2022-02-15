# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\main\migrations\0013_auto_20211231_1207.py
# Compiled at: 2021-12-31 12:07:02
# Size of source mod 2**32: 922 bytes
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('main', '0012_auto_20211230_1133')]
    operations = [
     migrations.AlterField(model_name='reportfiltermodel',
       name='filter_type',
       field=models.CharField(blank=True, choices=[('1', 'e'), ('2', 'ne'), ('3', 'gt'), ('4', 'gte'), ('5', 'lt'), ('6', 'lte'), ('7', 'in'), ('8', 'out'), ('9', 'limit'), ('10', 'last_in'), ('11', 'next_in'), ('12', 'order_by')], max_length=50, null=True, verbose_name='Tipi')),
     migrations.AlterField(model_name='reportmodel',
       name='report_type',
       field=models.CharField(blank=True, choices=[('1', 'Pie'), ('2', 'Line'), ('3', 'Bar')], max_length=50, null=True, verbose_name='Rapor Tipi'))]