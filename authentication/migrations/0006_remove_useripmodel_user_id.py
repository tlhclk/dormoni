# Generated by Django 3.2.5 on 2021-09-19 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_historylogmodel_ip_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useripmodel',
            name='user_id',
        ),
    ]