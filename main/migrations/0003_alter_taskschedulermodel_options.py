# Generated by Django 3.2.5 on 2021-10-02 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210919_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskschedulermodel',
            options={'ordering': ['-is_active', '-run_time'], 'verbose_name': 'Görev Zamanlayıcısı'},
        ),
    ]
