# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\parameters\models.py
# Compiled at: 2021-12-30 11:22:13
# Size of source mod 2**32: 15291 bytes
from django.db import models

class ContinentModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_continent'
        ordering = ['name']
        verbose_name = 'Kıta'

    def __str__(self):
        return '%s' % self.name


class CountryModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=20)
    continent_id = models.ForeignKey(verbose_name='Kıtası', null=True, blank=True, on_delete=(models.SET_NULL), to=ContinentModel)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_country'
        ordering = ['continent_id', 'name']
        verbose_name = 'Ülke'

    def __str__(self):
        return '%s > %s' % (str(self.continent_id), self.name)


class CityModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=20)
    country_id = models.ForeignKey(verbose_name='Ülkesi', null=True, blank=True, on_delete=(models.SET_NULL), to=CountryModel)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_city'
        ordering = ['country_id', 'name']
        verbose_name = 'Şehir'

    def __str__(self):
        return '%s > %s' % (str(self.country_id), self.name)


class TownModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=20)
    city_id = models.ForeignKey(verbose_name='İli', null=True, blank=True, on_delete=(models.SET_NULL), to=CityModel)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_town'
        ordering = ['city_id', 'name']
        verbose_name = 'İlçe Listesi'

    def __str__(self):
        return '%s > %s' % (self.city_id, self.name)


class CardTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_cardtype'
        ordering = ['name']
        verbose_name = 'Kart Türü Listesi'

    def __str__(self):
        return '%s' % self.name


class ChangePurposeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_changepurpose'
        ordering = ['name']
        verbose_name = 'Aldım - Verdim Amacı'

    def __str__(self):
        return '%s' % self.name


class RepetitiveTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_repetitivetype'
        ordering = ['name']
        verbose_name = 'Tekrarlı Olay Türü'

    def __str__(self):
        return '%s' % self.name


class CorporationTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_corporationtype'
        ordering = ['name']
        verbose_name = 'Firma Türü'

    def __str__(self):
        return '%s' % self.name


class MarketModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_market'
        ordering = ['name']
        verbose_name = 'Firma Sektörü'

    def __str__(self):
        return '%s' % self.name


class EmailTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_emailtype'
        ordering = ['name']
        verbose_name = 'E-Mail Türü'

    def __str__(self):
        return '%s' % self.name


class EventTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_eventtype'
        ordering = ['name']
        verbose_name = 'Etkinlik Türü'

    def __str__(self):
        return '%s' % self.name


class GenderModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_gender'
        ordering = ['name']
        verbose_name = 'Cinsiyet'

    def __str__(self):
        return '%s' % self.name


class MediaTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    base_url = models.CharField(verbose_name='Kaynak Url', null=True, blank=True, max_length=200)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_mediatype'
        ordering = ['name']
        verbose_name = 'Sosyal Medya Türü'


class PeriodModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    day = models.CharField(verbose_name='Gün', null=True, blank=True, max_length=4)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_period'
        ordering = ['name']
        verbose_name = 'Dönem'

    def __str__(self):
        return '%s' % self.name


class PhoneTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_phonetype'
        ordering = ['name']
        verbose_name = 'Telefon Türü'

    def __str__(self):
        return '%s' % self.name


class RelationTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=20)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_relationship'
        ordering = ['name']
        verbose_name = 'Kişi İlişkisi'

    def __str__(self):
        return '%s' % self.name


class SchoolTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_schooltype'
        ordering = ['name']
        verbose_name = 'Okul Türü'

    def __str__(self):
        return '%s' % self.name


class SeriesDownloadModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_download'
        ordering = ['name']
        verbose_name = 'Seri İndirilebilirliği'

    def __str__(self):
        return '%s' % self.name


class GenreModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_genre'
        ordering = ['name']
        verbose_name = 'Seri Tarzı'

    def __str__(self):
        return '%s' % self.name


class SeriesStateModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_seriesstate'
        ordering = ['name']
        verbose_name = 'Takip Durumu'

    def __str__(self):
        return '%s' % self.name


class SeriesTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_seriestype'
        ordering = ['name']
        verbose_name = 'Seri Türü'

    def __str__(self):
        return '%s' % self.name


class FinancialCategoryModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_financialcategory'
        ordering = ['name']
        verbose_name = 'Finans Kategorisi'

    def __str__(self):
        return '%s' % self.name


class TransactionTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_transactiontype'
        ordering = ['name']
        verbose_name = 'Muhasebe Türü'

    def __str__(self):
        return '%s' % self.name


class OperationTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=20)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_operationtype'
        ordering = ['name']
        verbose_name = 'İşlem Türü'

    def __str__(self):
        return '%s' % self.name


class AppTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_apptype'
        ordering = ['name']
        verbose_name = 'Uygulama Tipi'

    def __str__(self):
        return '%s' % self.name


class PathTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    icon_code = models.CharField(verbose_name='Sidebar İcon Kodu', null=True, blank=True, max_length=100)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_pathtype'
        ordering = ['name']
        verbose_name = 'Güzergah Tipi'

    def __str__(self):
        return '%s' % self.name


class ClothesTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_clothestype'
        ordering = ['name']
        verbose_name = 'Kıyafet Tipi'

    def __str__(self):
        return '%s' % self.name


class CarClassModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_carclass'
        ordering = ['name']
        verbose_name = 'Araba Sınıfı'

    def __str__(self):
        return '%s' % self.name


class CarTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_cartype'
        ordering = ['name']
        verbose_name = 'Cinsi'

    def __str__(self):
        return '%s' % self.name


class CarFuelTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_carfueltype'
        ordering = ['name']
        verbose_name = 'Yakıt Tipi'

    def __str__(self):
        return '%s' % self.name


class CarUsageModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_carusage'
        ordering = ['name']
        verbose_name = 'Kullanım Amacı'

    def __str__(self):
        return '%s' % self.name


class FunctionTypeModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=50)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_functiontype'
        ordering = ['name']
        verbose_name = 'Fonksiyon Tipi'

    def __str__(self):
        return '%s' % self.name