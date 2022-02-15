# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\schema\migrations\0009_auto_20211229_1215.py
# Compiled at: 2021-12-29 12:15:59
# Size of source mod 2**32: 1139 bytes
from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
     ('schema', '0008_auto_20211229_1054')]
    operations = [
     migrations.AddField(model_name='fieldmodel',
       name='related_name',
       field=models.CharField(blank=True, max_length=100, null=True, verbose_name='İlişki Adı')),
     migrations.AlterField(model_name='fieldmodel',
       name='auto_now',
       field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Otomatik Zaman Ekle')),
     migrations.AlterField(model_name='fieldmodel',
       name='auto_now_add',
       field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Otomatik Zamanı Düzenle')),
     migrations.AlterField(model_name='fieldmodel',
       name='on_delete',
       field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Silinme Şekli'))]