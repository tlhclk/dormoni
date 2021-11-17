# Generated by Django 3.2.5 on 2021-11-17 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schema', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('parameters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticationGroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, unique=True, verbose_name='Adı')),
                ('code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Kodu')),
            ],
            options={
                'verbose_name': 'Grup',
                'db_table': 'authentication_authentacationgroup',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AuthenticationUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.CharField(blank=True, max_length=200, null=True, verbose_name='Profil Fotoğrafı')),
                ('user_id', models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'verbose_name': 'Kullanıcı',
                'db_table': 'authentication_authenticationuser',
                'ordering': ['user_id'],
            },
        ),
        migrations.CreateModel(
            name='FieldPermissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adı')),
                ('action', models.CharField(blank=True, max_length=100, null=True, verbose_name='İşlem')),
                ('field_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schema.fieldmodel', verbose_name='Model Alanı')),
            ],
            options={
                'verbose_name': 'Model Alanı İzni',
                'db_table': 'authentication_fieldpermission',
                'ordering': ['field_id', 'action'],
                'unique_together': {('field_id', 'action')},
            },
        ),
        migrations.CreateModel(
            name='ObjectPermissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adı')),
                ('primary_key', models.CharField(blank=True, max_length=10, null=True, verbose_name='Birincil Anahtar')),
                ('action', models.CharField(blank=True, max_length=100, null=True, verbose_name='İşlem')),
                ('table_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schema.tablemodel', verbose_name='Tablo')),
            ],
            options={
                'verbose_name': 'Tablo Öğesi İzni',
                'db_table': 'authentication_objectpermission',
                'ordering': ['table_id', 'primary_key', 'action'],
                'unique_together': {('table_id', 'primary_key', 'action')},
            },
        ),
        migrations.CreateModel(
            name='TablePermissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adı')),
                ('action', models.CharField(blank=True, max_length=100, null=True, verbose_name='İşlem')),
                ('table_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schema.tablemodel', verbose_name='Tablo')),
            ],
            options={
                'verbose_name': 'Tablo İzni',
                'db_table': 'authentication_tablepermission',
                'ordering': ['table_id', 'action'],
                'unique_together': {('table_id', 'action')},
            },
        ),
        migrations.CreateModel(
            name='UserIpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(null=True, unique=True, verbose_name='IP Adres')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='Aktiflik')),
                ('permission', models.BooleanField(blank=True, default=False, null=True, verbose_name='İzin Durumu')),
                ('auth_key', models.CharField(max_length=200, null=True, unique=True, verbose_name='Yetki Anahtarı')),
                ('activation_date', models.DateTimeField(blank=True, null=True, verbose_name='Aktivasyon Zamanı')),
            ],
            options={
                'verbose_name': 'Kullanıcı Ipsi',
                'db_table': 'authentication_userip',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='OperationHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_key', models.CharField(blank=True, max_length=10, null=True, verbose_name='Birincil Anahtar')),
                ('detail', models.CharField(blank=True, max_length=200, null=True, verbose_name='Detay')),
                ('datetime', models.DateTimeField(blank=True, null=True, verbose_name='Zamanı')),
                ('table_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schema.tablemodel', verbose_name='Tablo')),
                ('type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parameters.operationtypemodel', verbose_name='Türü')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Sahibi')),
            ],
            options={
                'verbose_name': 'İşlem Geçmişi',
                'db_table': 'authentication_operationhistory',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='HistoryLogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Tarih')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Saat')),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name='IP Adres')),
                ('action', models.CharField(max_length=50, null=True, verbose_name='Eylem')),
                ('hyperlink', models.CharField(max_length=200, null=True, verbose_name='Bağlantı Adresi')),
                ('session', models.CharField(max_length=200, null=True, verbose_name='Oturum')),
                ('csrf_token', models.CharField(blank=True, max_length=200, null=True, verbose_name='Kontrol Anahtarı')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'verbose_name': 'Geçmiş Kayıt',
                'db_table': 'authentication_historylog',
                'ordering': ['-date', '-time'],
            },
        ),
        migrations.CreateModel(
            name='UserTablePermissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
                ('table_permission_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.tablepermissionmodel', verbose_name='Tablo Yetkisi')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.authenticationusermodel', verbose_name='Kullanıcı')),
            ],
            options={
                'verbose_name': 'Tablo Yetkisi Olan Kullanıcılar',
                'db_table': 'authentication_usertablepermission',
                'ordering': ['table_permission_id', 'user_id'],
                'unique_together': {('table_permission_id', 'user_id')},
            },
        ),
        migrations.CreateModel(
            name='UserObjectPermissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
                ('object_permission_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.objectpermissionmodel', verbose_name='Tablo Objesi Yetkisi')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.authenticationusermodel', verbose_name='Kullanıcı')),
            ],
            options={
                'verbose_name': 'Tablo Öğesi Yetkisi Olan Kullanıcılar',
                'db_table': 'authentication_userobjectpermission',
                'ordering': ['object_permission_id', 'user_id'],
                'unique_together': {('object_permission_id', 'user_id')},
            },
        ),
        migrations.CreateModel(
            name='UserGroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.authenticationgroupmodel', verbose_name='Grup')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.authenticationusermodel', verbose_name='Kullanıcı')),
            ],
            options={
                'verbose_name': 'Kullanıcı Grupları',
                'db_table': 'authentication_usergroup',
                'ordering': ['group_id', 'user_id'],
                'unique_together': {('user_id', 'group_id')},
            },
        ),
        migrations.CreateModel(
            name='UserFieldPermissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
                ('field_permission_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.fieldpermissionmodel', verbose_name='Model Alanı Yetkisi')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.authenticationusermodel', verbose_name='Kullanıcı')),
            ],
            options={
                'verbose_name': 'Model Alanı Yetkisi Olan Kullanıcılaar',
                'db_table': 'authentication_userfieldpermission',
                'ordering': ['field_permission_id', 'user_id'],
                'unique_together': {('field_permission_id', 'user_id')},
            },
        ),
        migrations.CreateModel(
            name='GroupTablePermissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.authenticationgroupmodel', verbose_name='Grup')),
                ('table_permission_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.tablepermissionmodel', verbose_name='Tablo Yetkisi')),
            ],
            options={
                'verbose_name': 'Tablo Yetkisi Olan Gruplar',
                'db_table': 'authentication_grouptablepermission',
                'ordering': ['table_permission_id', 'group_id'],
                'unique_together': {('table_permission_id', 'group_id')},
            },
        ),
        migrations.CreateModel(
            name='GroupObjectPermissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.authenticationgroupmodel', verbose_name='Grup')),
                ('object_permission_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.objectpermissionmodel', verbose_name='Tablo Objesi Yetkisi')),
            ],
            options={
                'verbose_name': 'Tablo Öğesi Yetkisi Olan Gruplar',
                'db_table': 'authentication_groupobjectpermission',
                'ordering': ['object_permission_id', 'group_id'],
                'unique_together': {('object_permission_id', 'group_id')},
            },
        ),
        migrations.CreateModel(
            name='GroupFieldPermissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
                ('field_permission_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.fieldpermissionmodel', verbose_name='Model Alanı Yetkisi')),
                ('group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.authenticationgroupmodel', verbose_name='Grup')),
            ],
            options={
                'verbose_name': 'Model Alanı Yetkisi Olan Gruplar',
                'db_table': 'authentication_groupfieldpermission',
                'ordering': ['field_permission_id', 'group_id'],
                'unique_together': {('field_permission_id', 'group_id')},
            },
        ),
    ]
