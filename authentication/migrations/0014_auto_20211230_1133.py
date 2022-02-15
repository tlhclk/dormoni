# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\authentication\migrations\0014_auto_20211230_1133.py
# Compiled at: 2021-12-30 11:33:55
# Size of source mod 2**32: 3122 bytes
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('authentication', '0013_auto_20211229_1054')]
    operations = [
     migrations.AddField(model_name='authenticationgroupmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='authenticationusermodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='fieldpermissionmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='groupfieldpermissionmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='groupobjectpermissionmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='grouptablepermissionmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='objectpermissionmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='tablepermissionmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='userfieldpermissionmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='usergroupmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='useripmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='userobjectpermissionmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
     migrations.AddField(model_name='usertablepermissionmodel',
       name='desc',
       field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama'))]