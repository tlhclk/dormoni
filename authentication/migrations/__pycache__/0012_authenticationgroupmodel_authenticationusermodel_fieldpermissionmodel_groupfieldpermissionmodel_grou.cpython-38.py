# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\authentication\migrations\0012_authenticationgroupmodel_authenticationusermodel_fieldpermissionmodel_groupfieldpermissionmodel_grou.py
# Compiled at: 2021-11-28 23:28:35
# Size of source mod 2**32: 11805 bytes
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
     migrations.swappable_dependency(settings.AUTH_USER_MODEL),
     ('people', '0003_auto_20211006_2156'),
     ('schema', '0005_auto_20211009_1333'),
     ('authentication', '0011_auto_20211006_2156')]
    operations = [
     migrations.CreateModel(name='AuthenticationGroupModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'name', models.CharField(blank=True, default='', max_length=200, unique=True, verbose_name='Adı')),
      (
       'code', models.CharField(blank=True, max_length=200, null=True, verbose_name='Kodu'))],
       options={'verbose_name':'Grup', 
      'db_table':'authentication_authentacationgroup', 
      'ordering':[
       'name']}),
     migrations.CreateModel(name='AuthenticationUserModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'profile_pic', models.CharField(blank=True, max_length=200, null=True, verbose_name='Profil Fotoğrafı')),
      (
       'person_id', models.OneToOneField(blank=True, default='', on_delete=(django.db.models.deletion.SET_DEFAULT), to='people.personmodel', verbose_name='Kişi')),
      (
       'user_id', models.OneToOneField(blank=True, default='', on_delete=(django.db.models.deletion.SET_DEFAULT), to=(settings.AUTH_USER_MODEL), verbose_name='Kullanıcı'))],
       options={'verbose_name':'Kullanıcı', 
      'db_table':'authentication_authenticationuser', 
      'ordering':[
       'user_id']}),
     migrations.CreateModel(name='FieldPermissionModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adı')),
      (
       'action', models.CharField(blank=True, max_length=100, null=True, verbose_name='İşlem')),
      (
       'field_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='schema.fieldmodel', verbose_name='Model Alanı'))],
       options={'verbose_name':'Model Alanı İzni', 
      'db_table':'authentication_fieldpermission', 
      'ordering':[
       'field_id', 'action'], 
      'unique_together':{
       ('field_id', 'action')}}),
     migrations.CreateModel(name='ObjectPermissionModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adı')),
      (
       'primary_key', models.CharField(blank=True, max_length=10, null=True, verbose_name='Birincil Anahtar')),
      (
       'action', models.CharField(blank=True, max_length=100, null=True, verbose_name='İşlem')),
      (
       'table_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='schema.tablemodel', verbose_name='Tablo'))],
       options={'verbose_name':'Tablo Öğesi İzni', 
      'db_table':'authentication_objectpermission', 
      'ordering':[
       'table_id', 'primary_key', 'action'], 
      'unique_together':{
       ('table_id', 'primary_key', 'action')}}),
     migrations.CreateModel(name='TablePermissionModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adı')),
      (
       'action', models.CharField(blank=True, max_length=100, null=True, verbose_name='İşlem')),
      (
       'table_id', models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.SET_NULL), to='schema.tablemodel', verbose_name='Tablo'))],
       options={'verbose_name':'Tablo İzni', 
      'db_table':'authentication_tablepermission', 
      'ordering':[
       'table_id', 'action'], 
      'unique_together':{
       ('table_id', 'action')}}),
     migrations.CreateModel(name='UserTablePermissionModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
      (
       'table_permission_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.tablepermissionmodel', verbose_name='Tablo Yetkisi')),
      (
       'user_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.authenticationusermodel', verbose_name='Kullanıcı'))],
       options={'verbose_name':'Tablo Yetkisi Olan Kullanıcılar', 
      'db_table':'authentication_usertablepermission', 
      'ordering':[
       'table_permission_id', 'user_id'], 
      'unique_together':{
       ('table_permission_id', 'user_id')}}),
     migrations.CreateModel(name='UserObjectPermissionModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
      (
       'object_permission_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.objectpermissionmodel', verbose_name='Tablo Objesi Yetkisi')),
      (
       'user_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.authenticationusermodel', verbose_name='Kullanıcı'))],
       options={'verbose_name':'Tablo Öğesi Yetkisi Olan Kullanıcılar', 
      'db_table':'authentication_userobjectpermission', 
      'ordering':[
       'object_permission_id', 'user_id'], 
      'unique_together':{
       ('object_permission_id', 'user_id')}}),
     migrations.CreateModel(name='UserGroupModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'group_id', models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.authenticationgroupmodel', verbose_name='Grup')),
      (
       'user_id', models.ForeignKey(blank=True, null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.authenticationusermodel', verbose_name='Kullanıcı'))],
       options={'verbose_name':'Kullanıcı Grupları', 
      'db_table':'authentication_usergroup', 
      'ordering':[
       'group_id', 'user_id'], 
      'unique_together':{
       ('user_id', 'group_id')}}),
     migrations.CreateModel(name='UserFieldPermissionModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
      (
       'field_permission_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.fieldpermissionmodel', verbose_name='Model Alanı Yetkisi')),
      (
       'user_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.authenticationusermodel', verbose_name='Kullanıcı'))],
       options={'verbose_name':'Model Alanı Yetkisi Olan Kullanıcılaar', 
      'db_table':'authentication_userfieldpermission', 
      'ordering':[
       'field_permission_id', 'user_id'], 
      'unique_together':{
       ('field_permission_id', 'user_id')}}),
     migrations.CreateModel(name='GroupTablePermissionModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
      (
       'group_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.authenticationgroupmodel', verbose_name='Grup')),
      (
       'table_permission_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.tablepermissionmodel', verbose_name='Tablo Yetkisi'))],
       options={'verbose_name':'Tablo Yetkisi Olan Gruplar', 
      'db_table':'authentication_grouptablepermission', 
      'ordering':[
       'table_permission_id', 'group_id'], 
      'unique_together':{
       ('table_permission_id', 'group_id')}}),
     migrations.CreateModel(name='GroupObjectPermissionModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
      (
       'group_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.authenticationgroupmodel', verbose_name='Grup')),
      (
       'object_permission_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.objectpermissionmodel', verbose_name='Tablo Objesi Yetkisi'))],
       options={'verbose_name':'Tablo Öğesi Yetkisi Olan Gruplar', 
      'db_table':'authentication_groupobjectpermission', 
      'ordering':[
       'object_permission_id', 'group_id'], 
      'unique_together':{
       ('object_permission_id', 'group_id')}}),
     migrations.CreateModel(name='GroupFieldPermissionModel',
       fields=[
      (
       'id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
      (
       'permission', models.BooleanField(default=False, verbose_name='Yetki Durumu')),
      (
       'field_permission_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.fieldpermissionmodel', verbose_name='Model Alanı Yetkisi')),
      (
       'group_id', models.ForeignKey(null=True, on_delete=(django.db.models.deletion.SET_NULL), to='authentication.authenticationgroupmodel', verbose_name='Grup'))],
       options={'verbose_name':'Model Alanı Yetkisi Olan Gruplar', 
      'db_table':'authentication_groupfieldpermission', 
      'ordering':[
       'field_permission_id', 'group_id'], 
      'unique_together':{
       ('field_permission_id', 'group_id')}})]