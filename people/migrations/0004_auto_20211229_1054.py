# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\people\migrations\0004_auto_20211229_1054.py
# Compiled at: 2021-12-29 10:54:58
# Size of source mod 2**32: 2004 bytes
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('people', '0003_auto_20211006_2156')]
    operations = [
     migrations.AlterField(model_name='educationmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='emailmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='personmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='phonemodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='photomodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='relationshipmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='relationshippersonmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='socialmediamodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'))]