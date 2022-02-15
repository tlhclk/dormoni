# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\authentication\migrations\0013_auto_20211229_1054.py
# Compiled at: 2021-12-29 10:54:57
# Size of source mod 2**32: 3743 bytes
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('authentication', '0012_authenticationgroupmodel_authenticationusermodel_fieldpermissionmodel_groupfieldpermissionmodel_grou')]
    operations = [
     migrations.AlterField(model_name='authenticationgroupmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='authenticationusermodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='fieldpermissionmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='groupfieldpermissionmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='groupobjectpermissionmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='grouptablepermissionmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='historylogmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='objectpermissionmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='operationhistorymodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='tablepermissionmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='userfieldpermissionmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='usergroupmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='useripmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='userobjectpermissionmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
     migrations.AlterField(model_name='usertablepermissionmodel',
       name='id',
       field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'))]