# Generated by Django 3.2.5 on 2021-10-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_useripmodel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historylogmodel',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='historylogmodel',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Saat'),
        ),
        migrations.AlterField(
            model_name='operationhistorymodel',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Zamanı'),
        ),
    ]
