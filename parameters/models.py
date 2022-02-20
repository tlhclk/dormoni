# -*- coding: utf-8 -*-
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


class PeopleGroupModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=50)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'parameters_group'
        ordering = ['name']
        verbose_name = 'Rehber Grubu'

    def __str__(self):
        return '%s' % self.name
