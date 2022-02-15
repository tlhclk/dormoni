# Generated by Django 3.2.5 on 2021-10-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0004_alter_tablemodel_app_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldmodel',
            name='form_create',
            field=models.BooleanField(default=True, verbose_name='Oluşturulabilir'),
        ),
        migrations.AlterField(
            model_name='fieldmodel',
            name='form_delete',
            field=models.BooleanField(default=True, verbose_name='Silinebilir'),
        ),
        migrations.AlterField(
            model_name='fieldmodel',
            name='form_update',
            field=models.BooleanField(default=True, verbose_name='Değiştirilebilir'),
        ),
        migrations.AlterField(
            model_name='fieldmodel',
            name='is_generated',
            field=models.BooleanField(default=False, verbose_name='Oluşturulan'),
        ),
        migrations.AlterField(
            model_name='fieldmodel',
            name='on_delete',
            field=models.CharField(blank=True, default='models.SET_NULL', max_length=100, null=True, verbose_name='Silinme Şekli'),
        ),
        migrations.AlterField(
            model_name='fieldmodel',
            name='show_detail',
            field=models.BooleanField(default=True, verbose_name='Detayda Gösterimi'),
        ),
        migrations.AlterField(
            model_name='fieldmodel',
            name='show_list',
            field=models.BooleanField(default=True, verbose_name='Listede Gösterimi'),
        ),
    ]
