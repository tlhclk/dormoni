# Generated by Django 3.2.5 on 2021-10-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_taskschedulermodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskschedulermodel',
            name='run_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Çalıştırma Zamanı'),
        ),
    ]
