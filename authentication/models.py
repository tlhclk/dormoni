# Create your models here.
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.hashers import make_password
from datetime import date
from django.contrib.auth.models import User
from schema.models import PathModel
from functions.db.manager import CustomManager


class CompanyModel(models.Model):
    company_status = models.CharField(verbose_name='Durumu',  max_length=20)
    registration_number = models.CharField(verbose_name='Sicil No',  max_length=20)
    chamber_registraion_sytem_no = models.CharField(verbose_name='Oda Sicil No',  max_length=20)
    company_title = models.CharField(verbose_name='Firma Ünvanı',  max_length=100)
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    second_name = models.CharField(verbose_name='İkincil Adı', null=True, blank=True, max_length=100)
    business_address = models.CharField(verbose_name='İş Adresi',  max_length=200)
    phone_number = models.CharField(verbose_name='Telefon No',  max_length=20)
    fax_number = models.CharField(verbose_name='Fax No', null=True, blank=True, max_length=20)
    hyperlink = models.CharField(verbose_name='Web Sayfası',  max_length=500)
    date_of_registration = models.DateField(verbose_name='Odaya Kayıt Tarihi', default=date.today)
    capital = models.CharField(verbose_name='Sermaye',  max_length=500)
    occupational_group = models.CharField(verbose_name='Meslek Grubu',  max_length=500)
    nace_codes = models.CharField(verbose_name='Nace Kodları',  max_length=500)
    desc  = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)
    objects = CustomManager()

    class Meta:
        db_table = 'authentication_company'
        ordering = ['company_title']
        verbose_name = 'Firma'

    def __str__(self):
        return '%s' % (self.company_title)


class BranchModel(models.Model):
    company_id = models.ForeignKey(verbose_name='Firma', on_delete=(models.CASCADE), to=CompanyModel,related_name="branch_info") 
    name = models.CharField(verbose_name='Adı', blank=True, max_length=200)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=200)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)
    objects = CustomManager()

    class Meta:
        db_table = 'authentication_branch'
        ordering = ['company_id','name']
        verbose_name = 'Firma Şubesi'
        unique_together=('company_id','name')

    def __str__(self):
        return '%s' % self.name


class AuthenticationGroupModel(models.Model):
    company_id = models.ForeignKey(verbose_name='Firma', null=True, blank=True,on_delete=(models.SET_NULL), to=CompanyModel,default="",related_name="group_info")
    branch_id = models.ForeignKey(verbose_name='Firma', on_delete=(models.CASCADE), to=BranchModel,default="",related_name="group_info") 
    name = models.CharField(verbose_name='Adı', blank=True, max_length=200)
    code = models.CharField(verbose_name='Kodu', null=True, blank=True, max_length=200)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)
    objects = CustomManager()

    class Meta:
        db_table = 'authentication_authentacationgroup'
        ordering = ['branch_id','name']
        verbose_name = 'Grup'
        unique_together=('branch_id','name')

    def __str__(self):
        return '%s' % self.name


class AuthenticationUserModel(models.Model):
    company_id = models.ForeignKey(verbose_name='Firma', null=True, blank=True,on_delete=(models.SET_NULL), to=CompanyModel,default="",related_name="user_info")
    branch_id = models.ForeignKey(verbose_name='Şube', null=True, blank=True,on_delete=(models.SET_NULL), to=BranchModel,default="",related_name="user_info")
    user_id = models.OneToOneField(verbose_name='Kullanıcı', unique=True, default='', blank=True, on_delete=(models.CASCADE), to=User,related_name="user_info")
    profile_pic = models.CharField(verbose_name='Profil Fotoğrafı', null=True, blank=True, max_length=200)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)
    objects = CustomManager()

    class Meta:
        db_table = 'authentication_authenticationuser'
        ordering = ['user_id']
        verbose_name = 'Kullanıcı'

    def __str__(self):
        return "%s > %s" %(self.company_id,self.user_id.get_full_name())



class UserGroupModel(models.Model):
    user_id = models.ForeignKey(verbose_name='Kullanıcı', on_delete=(models.CASCADE), to=AuthenticationUserModel,default="",related_name="usergroup_info")
    group_id = models.ForeignKey(verbose_name='Grup', on_delete=(models.CASCADE), to=AuthenticationGroupModel,default="",related_name="usergroup_info")
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)
    company_id = models.ForeignKey(verbose_name='Firma', null=True, blank=True,on_delete=(models.SET_NULL), to=CompanyModel,default="",related_name="usergroup_info")
    objects = CustomManager()

    class Meta:
        db_table = 'authentication_usergroup'
        ordering = ['group_id', 'user_id']
        verbose_name = 'Kullanıcı Grupları'
        unique_together = ('user_id', 'group_id')

    def __str__(self):
        return '%s > %s' % (self.group_id, self.user_id)

    def save(self):
        if self.user_id.company_id == self.group_id.branch_id.company_id:
            self.company_id=self.user_id.compant_id
            return super().save()
        else:
            raise ValueError("Kullanıcı ve Group Firmaları Aynı Değildir. Lütfen Aynı Firma Grubuna Atama Yapınız.")


class GroupPathModel(models.Model):
    group_id = models.ForeignKey(verbose_name='Grup', on_delete=(models.CASCADE), to=AuthenticationGroupModel,default="",related_name="userpath_info")
    path_id = models.ForeignKey(verbose_name='Güzergah', on_delete=(models.CASCADE), to=PathModel,default="",related_name="userpath_info")
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)
    company_id = models.ForeignKey(verbose_name='Firma', null=True, blank=True,on_delete=(models.SET_NULL), to=CompanyModel,default="",related_name="userpath_info")
    objects = CustomManager()

    
    class Meta:
        db_table = 'authentication_grouppath'
        ordering = ['path_id', 'group_id']
        verbose_name = 'Kullanıcı Grupları'
        unique_together = ('group_id', 'path_id')

    def __str__(self):
        return '%s > %s' % (str(self.path_id), str(self.group_id))
