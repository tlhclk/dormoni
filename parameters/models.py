# -*- coding: utf-8 -*-
### import_part
from django.db import models


### table_part
class ContinentModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_continent'
		ordering=['name']
		verbose_name='Kıta'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class CountryModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=20)
	continent_id = models.ForeignKey(verbose_name='Kıtası',null=True,blank=True,on_delete=models.SET_NULL,to=ContinentModel)

	class Meta:
		db_table='parameters_country'
		ordering=['continent_id', 'name']
		verbose_name='Ülke'

	def __str__(self):
		return "%s > %s" % (str(self.continent_id), self.name)



### table_part
class CityModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=20)
	country_id = models.ForeignKey(verbose_name='Ülkesi',null=True,blank=True,on_delete=models.SET_NULL,to=CountryModel)

	class Meta:
		db_table='parameters_city'
		ordering=['country_id', 'name']
		verbose_name='Şehir'

	def __str__(self):
		return "%s > %s" % (str(self.country_id), self.name)



### table_part
class TownModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=20)
	city_id = models.ForeignKey(verbose_name='İli',null=True,blank=True,on_delete=models.SET_NULL,to=CityModel)

	class Meta:
		db_table='parameters_town'
		ordering=['city_id', 'name']
		verbose_name='İlçe Listesi'

	def __str__(self):
		return "%s > %s" % (self.city_id, self.name)



### table_part
class CardTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_cardtype'
		ordering=['name']
		verbose_name='Kart Türü Listesi'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class ChangePurposeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_changepurpose'
		ordering=['name']
		verbose_name='Aldım - Verdim Amacı'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class RepetitiveTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_repetitivetype'
		ordering=['name']
		verbose_name='Tekrarlı Olay Türü'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class CorporationTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_corporationtype'
		ordering=['name']
		verbose_name='Firma Türü'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class MarketModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_market'
		ordering=['name']
		verbose_name='Firma Sektörü'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class EmailTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_emailtype'
		ordering=['name']
		verbose_name='E-Mail Türü'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class EventTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_eventtype'
		ordering=['name']
		verbose_name='Etkinlik Türü'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class GenderModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_gender'
		ordering=['name']
		verbose_name='Cinsiyet'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class MediaTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	base_url = models.CharField(verbose_name='Kaynak Url',null=True,blank=True,max_length=200)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_mediatype'
		ordering=['name']
		verbose_name='Sosyal Medya Türü'



### table_part
class PeriodModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	day = models.CharField(verbose_name='Gün',null=True,blank=True,max_length=4)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_period'
		ordering=['name']
		verbose_name='Dönem'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class PhoneTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_phonetype'
		ordering=['name']
		verbose_name='Telefon Türü'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class RelationTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=20)

	class Meta:
		db_table='parameters_relationship'
		ordering=['name']
		verbose_name='Kişi İlişkisi'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class SchoolTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_schooltype'
		ordering=['name']
		verbose_name='Okul Türü'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class SeriesDownloadModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_download'
		ordering=['name']
		verbose_name='Seri İndirilebilirliği'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class GenreModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_genre'
		ordering=['name']
		verbose_name='Seri Tarzı'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class SeriesStateModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_seriesstate'
		ordering=['name']
		verbose_name='Takip Durumu'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class SeriesTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_seriestype'
		ordering=['name']
		verbose_name='Seri Türü'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class FinancialCategoryModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_financialcategory'
		ordering=['name']
		verbose_name='Finans Kategorisi'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class TransactionTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_transactiontype'
		ordering=['name']
		verbose_name='Muhasebe Türü'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class OperationTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=50)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=20)

	class Meta:
		db_table='parameters_operationtype'
		ordering=['name']
		verbose_name='İşlem Türü'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class AppTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=50)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_apptype'
		ordering=['name']
		verbose_name='Uygulama Tipi'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class PathTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=50)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)
	icon_code = models.CharField(verbose_name='Sidebar İcon Kodu',null=True,blank=True,max_length=100)

	class Meta:
		db_table='parameters_pathtype'
		ordering=['name']
		verbose_name='Güzergah Tipi'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class ClothesTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=50)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_clothestype'
		ordering=['name']
		verbose_name='Kıyafet Tipi'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class CarClassModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=50)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_carclass'
		ordering=['name']
		verbose_name='Araba Sınıfı'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class CarTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=50)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_cartype'
		ordering=['name']
		verbose_name='Cinsi'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class CarFuelTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=50)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_carfueltype'
		ordering=['name']
		verbose_name='Yakıt Tipi'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class CarUsageModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=50)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_carusage'
		ordering=['name']
		verbose_name='Kullanım Amacı'

	def __str__(self):
		return "%s" % (self.name)



### table_part
class FunctionTypeModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=50)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=50)

	class Meta:
		db_table='parameters_functiontype'
		ordering=['name']
		verbose_name='Fonksiyon Tipi'

	def __str__(self):
		return "%s" % (self.name)

