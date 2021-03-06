# Generated by Django 3.2.5 on 2022-03-13 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0004_auto_20220313_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='SidebarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='Sıra No')),
                ('menu_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Menü Seviyesi')),
                ('desc', models.CharField(blank=True, max_length=200, null=True, verbose_name='Açıklama')),
                ('path_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sidebar_info', to='schema.pathmodel', verbose_name='Güzergah')),
            ],
            options={
                'verbose_name': 'Menü Güzergah',
                'db_table': 'schema_sidebar',
                'ordering': ['menu_code'],
            },
        ),
        migrations.RemoveField(
            model_name='parentpathmodel',
            name='path_id',
        ),
        migrations.DeleteModel(
            name='ChildPath',
        ),
        migrations.DeleteModel(
            name='ParentPathModel',
        ),
    ]
