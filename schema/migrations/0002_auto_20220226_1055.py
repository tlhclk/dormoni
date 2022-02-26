# Generated by Django 3.1.4 on 2022-02-26 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parameters', '0003_apptypemodel_pathtypemodel'),
        ('schema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Adı')),
                ('verbose_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Başlık')),
                ('sidebar_icon', models.CharField(blank=True, max_length=50, null=True, verbose_name='İcon')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
                ('type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.apptypemodel', verbose_name='Uygulama Türü')),
            ],
            options={
                'verbose_name': 'Uygulama',
                'db_table': 'schema_app',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='pathmodel',
            name='icon_code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Sidebar İcon Kodu'),
        ),
        migrations.AlterField(
            model_name='pathmodel',
            name='type_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.pathtypemodel', verbose_name='Güzergah Tipi'),
        ),
        migrations.CreateModel(
            name='TableModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Sıra No')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adı')),
                ('db_table', models.CharField(blank=True, max_length=50, null=True, verbose_name='Veritabanı Tablo Adı')),
                ('verbose_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Başlık')),
                ('list_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Liste Başlığı')),
                ('form_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Form Başlığı')),
                ('detail_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Detay Başlığı')),
                ('ordering', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sıralama')),
                ('verbose_name_plural', models.CharField(blank=True, max_length=100, null=True, verbose_name='Çoğul Başlık')),
                ('sidebar_icon', models.CharField(blank=True, max_length=50, null=True, verbose_name='İcon')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
                ('app_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schema.appmodel', verbose_name='Uygulama')),
            ],
            options={
                'verbose_name': 'Tablo',
                'db_table': 'schema_table',
                'ordering': ['app_id', 'order'],
            },
        ),
        migrations.CreateModel(
            name='FieldModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Sıra No')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adı')),
                ('verbose_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Başlık')),
                ('field', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alan Türü')),
                ('null', models.BooleanField(blank=True, default=True, null=True, verbose_name='Null ?')),
                ('blank', models.BooleanField(blank=True, default=True, null=True, verbose_name='Blank ?')),
                ('max_length', models.CharField(blank=True, max_length=5, null=True, verbose_name='En Fazla Uzunluk')),
                ('on_delete', models.CharField(blank=True, max_length=100, null=True, verbose_name='Silinme Şekli')),
                ('related_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='İlişki Adı')),
                ('to', models.CharField(blank=True, max_length=50, null=True, verbose_name='İlişkili Tablo')),
                ('default', models.CharField(blank=True, max_length=100, null=True, verbose_name='Varsayılan Değer')),
                ('max_digits', models.CharField(blank=True, max_length=5, null=True, verbose_name='En Fazla Hane')),
                ('decimal_places', models.CharField(blank=True, max_length=5, null=True, verbose_name='Virgülden Sonraki Hane')),
                ('is_generated', models.BooleanField(blank=True, default=False, null=True, verbose_name='Oluşturulan')),
                ('show_list', models.BooleanField(blank=True, default=True, null=True, verbose_name='Listede Gösterimi')),
                ('form_create', models.BooleanField(blank=True, default=True, null=True, verbose_name='Oluşturulabilir')),
                ('show_detail', models.BooleanField(blank=True, default=True, null=True, verbose_name='Detayda Gösterimi')),
                ('form_update', models.BooleanField(blank=True, default=True, null=True, verbose_name='Değiştirilebilir')),
                ('form_delete', models.BooleanField(default=True, verbose_name='Silinebilir')),
                ('help_text', models.CharField(blank=True, max_length=500, null=True, verbose_name='Yardımcı Metin')),
                ('error_messages', models.CharField(blank=True, max_length=500, null=True, verbose_name='Hata Mesajları')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Açıklama')),
                ('table_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schema.tablemodel', verbose_name='Model Adı')),
            ],
            options={
                'verbose_name': 'Model Alanı',
                'db_table': 'schema_field',
                'ordering': ['table_id', 'order'],
            },
        ),
        migrations.AddField(
            model_name='pathmodel',
            name='app_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schema.appmodel', verbose_name='Uygulama'),
        ),
    ]
