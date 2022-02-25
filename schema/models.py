# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.hashers import make_password
from datetime import date
from django.contrib.auth.models import User
from functions.queryset.manager import CustomManager


class PathModel(models.Model):
    title = models.CharField(verbose_name='Başlık',null=True,blank=True,max_length=100)
    name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
    path = models.CharField(verbose_name='Güzergah',null=True,blank=True,max_length=200)
    code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=100)
    type_id = models.CharField(verbose_name='Güzergah Tipi',null=True,blank=True,max_length=100)
    action = models.CharField(verbose_name='Eylemi',null=True,blank=True,max_length=100)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=100)
    objects = CustomManager()

    class Meta:
        db_table = 'schema_path'
        ordering = ['name']
        verbose_name = 'Güzergah'

    def __str__(self):
        return '%s' % (self.title)
    

class ParentPathModel(models.Model):
    path_id = models.ForeignKey(verbose_name='Güzergah', on_delete=(models.CASCADE), to=PathModel,default="",related_name="parentpath_info")
    menu_level = models.CharField(verbose_name='Menü Seviyesi',null=True,blank=True,max_length=100)
    order = models.CharField(verbose_name='Sıra No',null=True,blank=True,max_length=10)
    desc = models.CharField(verbose_name='Açıklama',null=True,blank=True,max_length=200)
    
    class Meta:
        db_table = 'schema_parentpath'
        ordering = ['order']
        verbose_name = 'Üst Menü Güzergah'

    def __str__(self):
        return '%s' % (str(self.path_id))

class ChildPath(models.Model):
    parentpath_id = models.ForeignKey(verbose_name='Güzergah', on_delete=(models.CASCADE), to=ParentPathModel,default="",related_name="childpath_info")
    path_id = models.ForeignKey(verbose_name='Güzergah', on_delete=(models.CASCADE), to=PathModel,default="",related_name="childpath_info")
    menu_level = models.CharField(verbose_name='Menü Seviyesi',null=True,blank=True,max_length=100)
    order = models.CharField(verbose_name='Sıra No',null=True,blank=True,max_length=10)
    desc = models.CharField(verbose_name='Açıklama',null=True,blank=True,max_length=200)
    
    class Meta:
        db_table = 'schema_childpath'
        ordering = ['order','parentpath_id']
        verbose_name = 'Alt Menü Güzergah'

    def __str__(self):
        return '%s > %s' % (str(self.parentpath_id),str(self.path_id))
