# Generated by Django 3.2.5 on 2021-09-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210919_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historylogmodel',
            name='app_id',
        ),
        migrations.RemoveField(
            model_name='historylogmodel',
            name='primary_key',
        ),
        migrations.AlterField(
            model_name='historylogmodel',
            name='action',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Eylem'),
        ),
    ]
