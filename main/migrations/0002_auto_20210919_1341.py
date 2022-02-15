# Generated by Django 3.2.5 on 2021-09-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corporationmodel',
            name='web_address',
        ),
        migrations.AddField(
            model_name='corporationmodel',
            name='hyperlink',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Bağlantı Adresi'),
        ),
    ]
