# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\main\migrations\0011_auto_20211229_1206.py
# Compiled at: 2021-12-29 12:06:10
# Size of source mod 2**32: 881 bytes
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
     ('main', '0010_auto_20211229_1204')]
    operations = [
     migrations.RenameField(model_name='reportmodel',
       old_name='date_field',
       new_name='date_field_id'),
     migrations.RenameField(model_name='reportmodel',
       old_name='group_by_field',
       new_name='group_by_field_id'),
     migrations.RenameField(model_name='reportmodel',
       old_name='text_field',
       new_name='text_field_id'),
     migrations.RenameField(model_name='reportmodel',
       old_name='value_field',
       new_name='value_field_id')]