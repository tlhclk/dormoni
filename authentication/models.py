# -*- coding: utf-8 -*-
### import_part
from typing import OrderedDict
from django.db import models
from django.contrib.auth.hashers import make_password
from datetime import date, datetime
from django.contrib.auth.models import User
from schema.models import TableModel,FieldModel
from parameters.models import OperationTypeModel

from django.contrib.auth.models import User

### table_part
class HistoryLogModel(models.Model):
	date = models.DateField(verbose_name='Tarih',blank=True,null=True)
	time = models.TimeField(verbose_name='Saat',blank=True,null=True)
	user_id = models.ForeignKey(verbose_name='Kullanıcı',null=True,blank=True,on_delete=models.SET_NULL,to=User)
	ip_address = models.GenericIPAddressField(verbose_name='IP Adres',max_length=50,null=True)
	action = models.CharField(max_length=50,verbose_name='Eylem',null=True)
	hyperlink = models.CharField(verbose_name='Bağlantı Adresi',max_length=200,null=True)
	session = models.CharField(verbose_name='Oturum',max_length=200,null=True)
	csrf_token = models.CharField(verbose_name='Kontrol Anahtarı',null=True,blank=True,max_length=200)

	class Meta:
		db_table='authentication_historylog'
		ordering=['-date', '-time']
		verbose_name='Geçmiş Kayıt'
	
	def logger_str(self):
		return "[%s] method: %s ,ip_address: %s,\tpath: %s,\tuser_id: %s,\tsesion_id: %s\t" % (self.action,self.date.strftime("%Y-%m-%d %H:%M:%S"), self.ip_address, self.hyperlink, self.user_id, self.session)
	
	def __str__(self):
		return str(self.date)+" - "+str(self.time)+" - "+str(self.user_id)+" - "+str(self.session)+" - "+str(self.csrf_token)+" - "+str(self.action)


### table_part
class OperationHistoryModel(models.Model):
	table_id = models.ForeignKey(verbose_name='Tablo',null=True,blank=True,on_delete=models.SET_NULL,to=TableModel)
	primary_key = models.CharField(verbose_name='Birincil Anahtar',null=True,blank=True,max_length=10)
	type_id = models.ForeignKey(verbose_name='Türü',null=True,blank=True,on_delete=models.SET_NULL,to=OperationTypeModel)
	detail = models.CharField(verbose_name='Detay',null=True,blank=True,max_length=200)
	datetime = models.DateTimeField(verbose_name='Zamanı',null=True,blank=True)
	user_id = models.ForeignKey(verbose_name='Sahibi',null=True,blank=True,on_delete=models.SET_NULL,to=User)

	class Meta:
		db_table='authentication_operationhistory'
		ordering=[]
		verbose_name='İşlem Geçmişi'

	def __str__(self):
		return "[%s] (%s) %s > %s : %s" % (self.datetime.strftime("%Y-%m-%d %H:%M:%S"),str(self.type_id),str(self.table_id),self.pk,self.detail)


### table_part
class UserIpModel(models.Model):
	ip_address = models.GenericIPAddressField(verbose_name='IP Adres',max_length=50,unique=True,null=True)
	is_active = models.BooleanField(verbose_name='Aktiflik',null=True,blank=True,default=True)
	permission = models.BooleanField(verbose_name='İzin Durumu',null=True,blank=True,default=False)
	auth_key = models.CharField(verbose_name='Yetki Anahtarı',max_length=200,unique=True,null=True)
	activation_date = models.DateTimeField(verbose_name="Aktivasyon Zamanı",null=True,blank=True)

	class Meta:
		db_table='authentication_userip'
		ordering=[]
		verbose_name='Kullanıcı Ipsi'

	def __str__(self):
		if self.activation_date:
			return "[%s] %s : %s" % (self.activation_date.strftime("%Y-%m-%d %H:%M:%S"),str(self.ip_address),str(self.permission))
		else:
			return "[%s] %s : %s" % ("",str(self.ip_address),str(self.permission))
			
	def get_auth_key(self):
		ip_list=self.ip_address.split(".")
		dt = datetime.now()
		auth_key_text="%s_%s-%s-%s-%s" % (dt.strftime("%y-%M-%d %H:%m:%s"),ip_list[0],ip_list[1],ip_list[2],ip_list[3])
		auth_key=make_password(auth_key_text)
		return auth_key
	
	def save(self, *args,**kwargs):
		print(*args)
		print(**kwargs)
		if self.auth_key=="":
			ip_list=self.ip_address.split(".")
			dt = datetime.now()
			auth_key_text="%s_%s-%s-%s-%s" % (dt.strftime("%y-%M-%d %H:%m:%s"),ip_list[0],ip_list[1],ip_list[2],ip_list[3])
			self.auth_key=make_password(auth_key_text)
			self.activation_date=dt
		return super().save( *args,**kwargs)


### table_part
class AuthenticationUserModel(models.Model):
	#["username","first_name","last_name","email","password","is_active","is_staff","is_superuser","date_joined","last_login"]
	user_id = models.OneToOneField(verbose_name='Kullanıcı',unique=True,default="",blank=True,on_delete=models.SET_DEFAULT,to=User)
	profile_pic= models.CharField(verbose_name="Profil Fotoğrafı",null=True,blank=True,max_length=200)

	class Meta:
		db_table='authentication_authenticationuser'
		ordering=['user_id']
		verbose_name='Kullanıcı'
	
	def  __str__(self):
		return "%s > %s" % (self.user_id,self.person_id)

### table_part
class AuthenticationGroupModel(models.Model):
	name= models.CharField(verbose_name="Adı",unique=True,default="",blank=True,max_length=200)
	code= models.CharField(verbose_name="Kodu",null=True,blank=True,max_length=200)

	class Meta:
		db_table='authentication_authentacationgroup'
		ordering=['name']
		verbose_name='Grup'
	
	def  __str__(self):
		return "%s" % (self.name)


### table_part
class UserGroupModel(models.Model):
	user_id = models.ForeignKey(verbose_name='Kullanıcı',null=True,blank=True,on_delete=models.SET_NULL,to=AuthenticationUserModel)
	group_id = models.ForeignKey(verbose_name='Grup',null=True,blank=True,on_delete=models.SET_NULL,to=AuthenticationGroupModel)
	
	class Meta:
		db_table='authentication_usergroup'
		ordering=['group_id','user_id']
		verbose_name='Kullanıcı Grupları'
		unique_together=('user_id','group_id')
	
	def  __str__(self):
		return "%s > %s" % (self.group_id,self.user_id)


### table_part
class TablePermissionModel(models.Model):
	name = models.CharField(verbose_name="Adı",null=True,blank=True,max_length=100)
	table_id = models.ForeignKey(verbose_name='Tablo',null=True,blank=True,on_delete=models.SET_NULL,to=TableModel)
	action = models.CharField(verbose_name="İşlem",null=True,blank=True,max_length=100)

	class Meta:
		db_table='authentication_tablepermission'
		ordering=['table_id','action']
		verbose_name='Tablo İzni'
		unique_together=('table_id','action')
	
	def  __str__(self):
		return "%s > %s" % (self.table_id,self.action)


### table_part
class FieldPermissionModel(models.Model):
	name = models.CharField(verbose_name="Adı",null=True,blank=True,max_length=100)
	field_id = models.ForeignKey(verbose_name='Model Alanı',null=True,blank=False,on_delete=models.SET_NULL,to=FieldModel)
	action = models.CharField(verbose_name="İşlem",null=True,blank=True,max_length=100)

	class Meta:
		db_table='authentication_fieldpermission'
		ordering=['field_id','action']
		verbose_name='Model Alanı İzni'
		unique_together=('field_id','action')
	
	def  __str__(self):
		return "%s > %s" % (self.field_id,self.action)


### table_part
class ObjectPermissionModel(models.Model):
	name = models.CharField(verbose_name="Adı",null=True,blank=True,max_length=100)
	table_id = models.ForeignKey(verbose_name='Tablo',null=True,blank=False,on_delete=models.SET_NULL,to=TableModel)
	primary_key = models.CharField(verbose_name='Birincil Anahtar',null=True,blank=True,max_length=10)
	action = models.CharField(verbose_name="İşlem",null=True,blank=True,max_length=100)

	class Meta:
		db_table='authentication_objectpermission'
		ordering=['table_id','primary_key','action']
		verbose_name='Tablo Öğesi İzni'
		unique_together=('table_id','primary_key','action')
	
	def  __str__(self):
		return "%s > %s > %s" % (self.table_id,self.primary_key,self.action)


### table_part
class UserTablePermissionModel(models.Model):
	user_id = models.ForeignKey(verbose_name='Kullanıcı',null=True,blank=False,on_delete=models.SET_NULL,to=AuthenticationUserModel)
	table_permission_id = models.ForeignKey(verbose_name='Tablo Yetkisi',null=True,blank=False,on_delete=models.SET_NULL,to=TablePermissionModel)
	permission= models.BooleanField(verbose_name='Yetki Durumu',default=False)
	
	class Meta:
		db_table='authentication_usertablepermission'
		ordering=['table_permission_id','user_id']
		verbose_name='Tablo Yetkisi Olan Kullanıcılar'
		unique_together=('table_permission_id','user_id')
	
	def  __str__(self):
		return "%s > %s" % (self.table_permission_id,self.user_id)


### table_part
class UserFieldPermissionModel(models.Model):
	user_id = models.ForeignKey(verbose_name='Kullanıcı',null=True,blank=False,on_delete=models.SET_NULL,to=AuthenticationUserModel)
	field_permission_id = models.ForeignKey(verbose_name='Model Alanı Yetkisi',null=True,blank=False,on_delete=models.SET_NULL,to=FieldPermissionModel)
	permission= models.BooleanField(verbose_name='Yetki Durumu',default=False)
	
	class Meta:
		db_table='authentication_userfieldpermission'
		ordering=['field_permission_id','user_id']
		verbose_name='Model Alanı Yetkisi Olan Kullanıcılaar'
		unique_together=('field_permission_id','user_id')
	
	def  __str__(self):
		return "%s > %s" % (self.field_permission_id,self.user_id)


### table_part
class UserObjectPermissionModel(models.Model):
	user_id = models.ForeignKey(verbose_name='Kullanıcı',null=True,blank=False,on_delete=models.SET_NULL,to=AuthenticationUserModel)
	object_permission_id = models.ForeignKey(verbose_name='Tablo Objesi Yetkisi',null=True,blank=False,on_delete=models.SET_NULL,to=ObjectPermissionModel)
	permission= models.BooleanField(verbose_name='Yetki Durumu',default=False)
	
	class Meta:
		db_table='authentication_userobjectpermission'
		ordering=['object_permission_id','user_id']
		verbose_name='Tablo Öğesi Yetkisi Olan Kullanıcılar'
		unique_together=('object_permission_id','user_id')
	
	def  __str__(self):
		return "%s > %s" % (self.object_permission_id,self.user_id)


### table_part
class GroupTablePermissionModel(models.Model):
	group_id = models.ForeignKey(verbose_name='Grup',null=True,blank=False,on_delete=models.SET_NULL,to=AuthenticationGroupModel)
	table_permission_id = models.ForeignKey(verbose_name='Tablo Yetkisi',null=True,blank=False,on_delete=models.SET_NULL,to=TablePermissionModel)
	permission= models.BooleanField(verbose_name='Yetki Durumu',default=False)
	
	class Meta:
		db_table='authentication_grouptablepermission'
		ordering=['table_permission_id','group_id']
		verbose_name='Tablo Yetkisi Olan Gruplar'
		unique_together=('table_permission_id','group_id')
	
	def  __str__(self):
		return "%s > %s" % (self.table_permission_id,self.group_id)


### table_part
class GroupFieldPermissionModel(models.Model):
	group_id = models.ForeignKey(verbose_name='Grup',null=True,blank=False,on_delete=models.SET_NULL,to=AuthenticationGroupModel)
	field_permission_id = models.ForeignKey(verbose_name='Model Alanı Yetkisi',null=True,blank=False,on_delete=models.SET_NULL,to=FieldPermissionModel)
	permission= models.BooleanField(verbose_name='Yetki Durumu',default=False)
	
	class Meta:
		db_table='authentication_groupfieldpermission'
		ordering=['field_permission_id','group_id']
		verbose_name='Model Alanı Yetkisi Olan Gruplar'
		unique_together=('field_permission_id','group_id')
	
	def  __str__(self):
		return "%s > %s" % (self.field_permission_id,self.group_id)


### table_part
class GroupObjectPermissionModel(models.Model):
	group_id = models.ForeignKey(verbose_name='Grup',null=True,blank=False,on_delete=models.SET_NULL,to=AuthenticationGroupModel)
	object_permission_id = models.ForeignKey(verbose_name='Tablo Objesi Yetkisi',null=True,blank=False,on_delete=models.SET_NULL,to=ObjectPermissionModel)
	permission= models.BooleanField(verbose_name='Yetki Durumu',default=False)
	
	class Meta:
		db_table='authentication_groupobjectpermission'
		ordering=['object_permission_id','group_id']
		verbose_name='Tablo Öğesi Yetkisi Olan Gruplar'
		unique_together=('object_permission_id','group_id')
	
	def  __str__(self):
		return "%s > %s" % (self.object_permission_id,self.group_id)