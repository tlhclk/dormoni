# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: C:\Users\talha.celik\Desktop\Talha\myerpv2-main\people\models.py
# Compiled at: 2022-01-01 12:24:16
# Size of source mod 2**32: 7543 bytes
from django.db import models
from parameters.models import GenderModel, CountryModel, CityModel, EmailTypeModel, PhoneTypeModel, MediaTypeModel, RelationTypeModel, SchoolTypeModel
from main.models import PeopleGroupModel, SchoolModel, DepartmentModel
from datetime import datetime

class PersonModel(models.Model):
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=20)
    full_name = models.CharField(verbose_name='Tam Adı', null=True, blank=True, max_length=100)
    id_number = models.CharField(verbose_name='Kimlik Numarası', null=True, blank=True, max_length=11)
    first_name = models.CharField(verbose_name='İlk Adı', null=True, blank=True, max_length=50)
    second_name = models.CharField(verbose_name='İkinci Adı', null=True, blank=True, max_length=50)
    middle_name = models.CharField(verbose_name='Ek Adı', null=True, blank=True, max_length=50)
    last_name = models.CharField(verbose_name='Soyadı', null=True, blank=True, max_length=50)
    nick_name = models.CharField(verbose_name='Takma Adı', null=True, blank=True, max_length=50)
    title = models.CharField(verbose_name='Ünvanı', null=True, blank=True, max_length=100)
    gender_id = models.ForeignKey(verbose_name='Cinsiyeti', null=True, blank=True, on_delete=(models.SET_NULL), to=GenderModel)
    group_id = models.ForeignKey(verbose_name='Grubu', null=True, blank=True, on_delete=(models.SET_NULL), to=PeopleGroupModel)
    date_of_birth = models.DateField(verbose_name='Doğum Tarihi', null=True, blank=True)
    hometown = models.CharField(verbose_name='Memleketi', null=True, blank=True, max_length=50)
    country_id = models.ForeignKey(verbose_name='Ülkesi', null=True, blank=True, on_delete=(models.SET_NULL), to=CountryModel)
    city_id = models.ForeignKey(verbose_name='İli', null=True, blank=True, on_delete=(models.SET_NULL), to=CityModel)
    address = models.CharField(verbose_name='Adresi', null=True, blank=True, max_length=200)
    date_of_death = models.DateField(verbose_name='Ölüm Tarihi', null=True, blank=True)
    favorite = models.BooleanField(verbose_name='Favori', null=True, blank=True, default=0)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'people_person'
        ordering = ['full_name']
        verbose_name = 'Rehber'

    def __str__(self):
        return '%s' % self.full_name

    def save(self, *args, **kwargs):
        name_list = [
         self.first_name]
        if self.second_name:
            name_list.append(self.second_name)
        if self.middle_name:
            name_list.append(self.middle_name)
        if self.last_name:
            name_list.append(self.last_name)
        self.full_name = ' '.join(name_list)
        return (super().save)(*args, **kwargs)


class EducationModel(models.Model):
    person_id = models.ForeignKey(verbose_name='Kim', null=True, blank=True, on_delete=(models.SET_NULL), to=PersonModel)
    schooltype_id = models.ForeignKey(verbose_name='Okul Tipi', null=True, blank=True, on_delete=(models.SET_NULL), to=SchoolTypeModel)
    school_id = models.ForeignKey(verbose_name='Okul', null=True, blank=True, on_delete=(models.SET_NULL), to=SchoolModel)
    department_id = models.ForeignKey(verbose_name='Bölümü', null=True, blank=True, on_delete=(models.SET_NULL), to=DepartmentModel)
    graduation_year = models.CharField(verbose_name='Mezuniyet Yılı', null=True, blank=True, max_length=4)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'people_education'
        ordering = ['person_id']
        verbose_name = 'Kişi Eğitimi'

    def __str__(self):
        return '%s > %s > %s' % (self.person_id, self.school_id, self.department_id)


class EmailModel(models.Model):
    person_id = models.ForeignKey(verbose_name='Kimin', null=True, blank=True, on_delete=(models.SET_NULL), to=PersonModel)
    email_type_id = models.ForeignKey(verbose_name='E-Mail Tipi', null=True, blank=True, on_delete=(models.SET_NULL), to=EmailTypeModel)
    email = models.EmailField(verbose_name='E-Mail Adresi', null=True, blank=True, max_length=100)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'people_email'
        ordering = ['person_id']
        verbose_name = 'Kişi E-Posta Adresi'

    def __str__(self):
        return '%s > %s' % (self.person_id, self.email)


class PhoneModel(models.Model):
    person_id = models.ForeignKey(verbose_name='Kimin', null=True, blank=True, on_delete=(models.SET_NULL), to=PersonModel)
    phone_type_id = models.ForeignKey(verbose_name='Telefon Tipi', null=True, blank=True, on_delete=(models.SET_NULL), to=PhoneTypeModel)
    phone_number = models.CharField(verbose_name='Telefon Numarası', null=True, blank=True, max_length=20)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'people_phone'
        ordering = ['person_id']
        verbose_name = 'Telefonu Numarası'

    def __str__(self):
        return '%s > %s' % (self.person_id, self.phone_number)


class PhotoModel(models.Model):
    person_id = models.ForeignKey(verbose_name='Kimin', null=True, blank=True, on_delete=(models.SET_NULL), to=PersonModel)
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    hyperlink = models.CharField(verbose_name='Bağlantı Adresi', null=True, blank=True, max_length=200)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'people_photo'
        ordering = ['person_id']
        verbose_name = 'Kişi Fotoğrafı'

    def __str__(self):
        return '%s > %s' % (self.person_id, self.name)


class SocialMediaModel(models.Model):
    person_id = models.ForeignKey(verbose_name='Kimin', null=True, blank=True, on_delete=(models.SET_NULL), to=PersonModel)
    media_type_id = models.ForeignKey(verbose_name='Sosyal Medya Tipi', null=True, blank=True, on_delete=(models.SET_NULL), to=MediaTypeModel)
    username = models.CharField(verbose_name='Kullanıcı Adı', null=True, blank=True, max_length=50)
    hyperlink = models.CharField(verbose_name='Bağlantı Adresi', null=True, blank=True, max_length=200)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'people_socialmedia'
        ordering = ['person_id']
        verbose_name = 'Sosyal Medya Hesabı'

    def __str__(self):
        return '%s > %s > %s' % (self.person_id, self.media_type_id, self.username)


class RelationshipModel(models.Model):
    person_id = models.ForeignKey(verbose_name='Kişi', null=True, blank=True, on_delete=(models.SET_NULL), to=PersonModel)
    relation_id = models.ForeignKey(verbose_name='İlişki', null=True, blank=True, on_delete=(models.SET_NULL), to=RelationTypeModel)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'people_relationtree'
        ordering = ['person_id', 'relation_id']
        verbose_name = 'Rehber İlişkisi'

    def __str__(self):
        return '%s: %s' % (self.relation_id, self.person_id)


class RelationshipPersonModel(models.Model):
    person_id = models.ForeignKey(verbose_name='Kişi', null=True, blank=True, on_delete=(models.SET_NULL), to=PersonModel)
    relation_tree_id = models.ForeignKey(verbose_name='İlişki Ağacı', null=True, blank=True, on_delete=(models.SET_NULL), to=RelationshipModel)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'people_relationtreeperson'
        ordering = ['person_id', 'relation_tree_id']
        verbose_name = 'İlişki Ağacı - Kişi'

    def __str__(self):
        return '%s <> %s' % (self.relation_tree_id, self.person_id)