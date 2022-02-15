# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\schema\migrations\0008_auto_20211229_1054.py
# Compiled at: 2021-12-29 10:54:58
# Size of source mod 2**32: 1325 bytes
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('schema', '0007_auto_20211107_1226')]
    operations = [
     migrations.AlterField(model_name='appmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='fieldmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='functionmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='pathmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='tablemodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'))]