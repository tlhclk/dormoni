# -*- coding: utf-8 -*-
### import_part
from django.db import models

from parameters.models import MarketModel,CorporationTypeModel,CityModel,TownModel,SchoolTypeModel,PeriodModel
from datetime import datetime


### table_part
class DepartmentModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='main_department'
		ordering=['name']
		verbose_name='Bölüm'
	
	def __str__(self):
		return "%s" % (self.name)



### table_part
class CorporationModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	market_id = models.ForeignKey(verbose_name='Market Tipi',null=True,blank=True,on_delete=models.SET_NULL,to=MarketModel)
	type_id = models.ForeignKey(verbose_name='Firma Tipi',null=True,blank=True,on_delete=models.SET_NULL,to=CorporationTypeModel)
	city_id = models.ForeignKey(verbose_name='İli',null=True,blank=True,on_delete=models.SET_NULL,to=CityModel)
	town_id = models.ForeignKey(verbose_name='İlçesi',null=True,blank=True,on_delete=models.SET_NULL,to=TownModel)
	hyperlink = models.CharField(verbose_name='Bağlantı Adresi',null=True,blank=True,max_length=200)
	address = models.CharField(verbose_name='Adresi',null=True,blank=True,max_length=200)
	phone_number = models.CharField(verbose_name='Telefon Numarası',null=True,blank=True,max_length=20)

	class Meta:
		db_table='main_corporation'
		ordering=['name']
		verbose_name='Firma'
	
	def __str__(self):
		return "%s" % (self.name)



### table_part
class PeopleGroupModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='main_group'
		ordering=['name']
		verbose_name='Rehber Grubu'
	
	def __str__(self):
		return "%s" % (self.name)



### table_part
class SchoolModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	type_id = models.ForeignKey(verbose_name='Okul Tipi',null=True,blank=True,on_delete=models.SET_NULL,to=SchoolTypeModel)
	city_id = models.ForeignKey(verbose_name='İli',null=True,blank=True,on_delete=models.SET_NULL,to=CityModel)

	class Meta:
		db_table='main_school'
		ordering=['city_id', 'name']
		verbose_name='Okul'
	
	def __str__(self):
		return "%s > %s" % (self.city_id,self.name)



### table_part
class TaskSchedulerModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=50)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)
	period_id = models.ForeignKey(verbose_name='Period Sıklığı',null=True,blank=True,on_delete=models.SET_NULL,to=PeriodModel)
	period_amount = models.CharField(verbose_name='Period Miktarı',null=True,blank=True,max_length=10)
	run_time = models.DateTimeField(verbose_name='Çalıştırma Zamanı',null=True,blank=True)
	run_func = models.CharField(verbose_name='Çalıştırılacak Fonksiyon',null=True,blank=True,max_length=200)
	is_active = models.BooleanField(verbose_name='Aktif Mi?',null=True,blank=True,default=0)

	class Meta:
		db_table='main_taskscheduler'
		ordering=["-is_active","-run_time"]
		verbose_name='Görev Zamanlayıcısı'
	
	def __str__(self):
		return "[%s] %s" % (self.last_date.strftime("%Y-%m-%d"),self.name)

