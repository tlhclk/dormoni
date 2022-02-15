# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\people\migrations\0005_auto_20211230_1133.py
# Compiled at: 2021-12-30 11:33:56
# Size of source mod 2**32: 1948 bytes
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('people', '0004_auto_20211229_1054')]
    operations = [
     migrations.AddField(model_name='educationmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='emailmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='personmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='phonemodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='photomodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='relationshipmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='relationshippersonmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='socialmediamodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama'))]