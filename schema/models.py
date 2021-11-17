# -*- coding: utf-8 -*-
### import_part
from django.db import models

from parameters.models import AppTypeModel,PathTypeModel


### table_part
class AppModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=50)
	type_id = models.ForeignKey(verbose_name='Uygulama Türü',null=True,blank=True,on_delete=models.SET_NULL,to=AppTypeModel)
	verbose_name = models.CharField(verbose_name='Başlık',null=True,blank=True,max_length=100)
	sidebar_icon = models.CharField(verbose_name='İcon',null=True,blank=True,max_length=50)
 
	class Meta:
		db_table='schema_app'
		ordering=['name']
		verbose_name='Uygulama'
	
	def __str__(self):
		return "%s" % (self.verbose_name)
	

### table_part
class TableModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	db_table = models.CharField(verbose_name='Veritabanı Tablo Adı',null=True,blank=True,max_length=50)
	verbose_name = models.CharField(verbose_name='Başlık',null=True,blank=True,max_length=100)
	list_title = models.CharField(verbose_name='Liste Başlığı',null=True,blank=True,max_length=200)
	form_title = models.CharField(verbose_name='Form Başlığı',null=True,blank=True,max_length=50)
	detail_title = models.CharField(verbose_name='Detay Başlığı',null=True,blank=True,max_length=50)
	app_id = models.ForeignKey(verbose_name='Uygulama',null=True,blank=True,on_delete=models.SET_NULL,to=AppModel)
	ordering = models.CharField(verbose_name='Sıralama',null=True,blank=True,max_length=100)
	order = models.IntegerField(verbose_name='Sıra No',null=True,blank=True)
	verbose_name_plural = models.CharField(verbose_name='Çoğul Başlık',null=True,blank=True,max_length=100)
	sidebar_icon = models.CharField(verbose_name='İcon',null=True,blank=True,max_length=50)

	class Meta:
		db_table='schema_table'
		ordering=['app_id', 'order']
		verbose_name='Tablo'
	
	def __str__(self):
		return "%s > %s"% (self.app_id,self.verbose_name)


### table_part
class FieldModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	verbose_name = models.CharField(verbose_name='Başlık',null=True,blank=True,max_length=100)
	field = models.CharField(verbose_name='Alan Türü',null=True,blank=True,max_length=100)
	table_id = models.ForeignKey(verbose_name='Model Adı',null=True,blank=True,on_delete=models.SET_NULL,to=TableModel)
	null = models.BooleanField(verbose_name='Null ?',null=True,blank=True,default=True)
	blank = models.BooleanField(verbose_name='Blank ?',null=True,blank=True,default=True)
	max_length = models.CharField(verbose_name='En Fazla Uzunluk',null=True,blank=True,max_length=5)
	on_delete = models.CharField(verbose_name='Silinme Şekli',null=True,blank=True,max_length=100,default='models.SET_NULL')
	to = models.CharField(verbose_name='İlişkili Tablo',null=True,blank=True,max_length=50)
	default = models.CharField(verbose_name='Varsayılan Değer',null=True,blank=True,max_length=100)
	max_digits = models.CharField(verbose_name='En Fazla Hane',null=True,blank=True,max_length=5)
	decimal_places = models.CharField(verbose_name='Virgülden Sonraki Hane',null=True,blank=True,max_length=5)
	is_generated = models.BooleanField(verbose_name='Oluşturulan',default=False,null=True,blank=True)
	show_list = models.BooleanField(verbose_name='Listede Gösterimi',default=True,null=True,blank=True)
	form_create = models.BooleanField(verbose_name='Oluşturulabilir',default=True,null=True,blank=True)
	show_detail = models.BooleanField(verbose_name='Detayda Gösterimi',default=True,null=True,blank=True)
	form_update = models.BooleanField(verbose_name='Değiştirilebilir',default=True,null=True,blank=True)
	form_delete = models.BooleanField(verbose_name='Silinebilir',default=True)
	order = models.IntegerField(verbose_name='Sıra No',null=True,blank=True)
	help_text = models.CharField(verbose_name='Yardımcı Metin',null=True,blank=True,max_length=500)
	error_messages = models.CharField(verbose_name='Hata Mesajları',null=True,blank=True,max_length=500)
	auto_now = models.CharField(verbose_name='Otomatik Zaman Ekle',null=True,blank=True,max_length=5,default=True)
	auto_now_add = models.CharField(verbose_name='Otomatik Zamanı Düzenle',null=True,blank=True,max_length=5,default=True)

	class Meta:
		db_table='schema_field'
		ordering=['table_id', 'order']
		verbose_name='Model Alanı'
	
	def __str__(self):
		return "%s > %s"% (self.table_id.verbose_name,self.verbose_name)


### table_part
class PathModel(models.Model):
	title = models.CharField(verbose_name='Başlık',null=True,blank=True,max_length=100)
	path = models.CharField(verbose_name='Güzergah',null=True,blank=True,max_length=100)
	view_func = models.CharField(verbose_name='View Fonksiyonu',null=True,blank=True,max_length=100)
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	app_id = models.ForeignKey(verbose_name='Uygulama',null=True,blank=True,on_delete=models.SET_NULL,to=AppModel)
	type_id = models.ForeignKey(verbose_name='Güzergah Tipi',null=True,blank=True,on_delete=models.SET_NULL,to=PathTypeModel)
	location = models.CharField(verbose_name='Konumu',null=True,blank=True,max_length=100)
	icon_code = models.CharField(verbose_name='Sidebar İcon Kodu',null=True,blank=True,max_length=100)

	class Meta:
		db_table='schema_path'
		ordering=['app_id', 'name']
		verbose_name='Güzergah Listesi'
	
	def __str__(self):
		return "%s >%s"% (self.app_id,self.title)

