# Generated by Django 3.2.5 on 2021-09-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210919_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historylogmodel',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, unique=True, verbose_name='IP Adres'),
        ),
        migrations.AlterField(
            model_name='useripmodel',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, unique=True, verbose_name='IP Adres'),
        ),
    ]