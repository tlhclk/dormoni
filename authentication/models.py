# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.hashers import make_password
from datetime import date, datetime
from django.contrib.auth.models import User
from schema.models import TableModel, FieldModel
from parameters.models import OperationTypeModel
from django.contrib.auth.models import User
from functions.manager import CustomManager


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
    branch_id = models.ForeignKey(verbose_name='Şube', on_delete=(models.CASCADE), to=BranchModel,default="",related_name="group_info") 
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
    company_id = models.ForeignKey(verbose_name='Firma', null=True, blank=True,on_delete=(models.CASCADE), to=CompanyModel,default="",related_name="user_info")
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
    company_id = models.ForeignKey(verbose_name='Firma', null=True, blank=True,on_delete=(models.CASCADE), to=CompanyModel,default="",related_name="usergroup_info")
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





class HistoryLogModel(models.Model):
    date = models.DateField(verbose_name='Tarih', blank=True, null=True)
    time = models.TimeField(verbose_name='Saat', blank=True, null=True)
    user_id = models.ForeignKey(verbose_name='Kullanıcı', null=True, blank=True, on_delete=(models.SET_NULL), to=User,related_name="history_info")
    ip_address = models.GenericIPAddressField(verbose_name='IP Adres', max_length=50, null=True)
    action = models.CharField(max_length=50, verbose_name='Eylem', null=True)
    hyperlink = models.CharField(verbose_name='Bağlantı Adresi', max_length=200, null=True)
    session = models.CharField(verbose_name='Oturum', max_length=200, null=True)
    csrf_token = models.CharField(verbose_name='Kontrol Anahtarı', null=True, blank=True, max_length=200)
    branch_id = models.ForeignKey(verbose_name='Şube', on_delete=(models.CASCADE), to=BranchModel,default="",related_name="history_info") 
    company_id = models.ForeignKey(verbose_name='Firma', null=True, blank=True,on_delete=(models.CASCADE), to=CompanyModel,default="",related_name="history_info")
    objects = CustomManager()

    class Meta:
        db_table = 'authentication_historylog'
        ordering = ['-date', '-time']
        verbose_name = 'Geçmiş Kayıt'

    def logger_str(self):
        return '[%s] method: %s ,ip_address: %s,\tpath: %s,\tuser_id: %s,\tsesion_id: %s\t' % (self.action, self.date.strftime('%Y-%m-%d %H:%M:%S'), self.ip_address, self.hyperlink, self.user_id, self.session)

    def __str__(self):
        return str(self.date) + ' - ' + str(self.time) + ' - ' + str(self.user_id) + ' - ' + str(self.session) + ' - ' + str(self.csrf_token) + ' - ' + str(self.action)


class OperationHistoryModel(models.Model):
    table_id = models.ForeignKey(verbose_name='Tablo', null=True, blank=True, on_delete=(models.SET_NULL), to=TableModel,related_name="operation_info")
    primary_key = models.CharField(verbose_name='Birincil Anahtar', null=True, blank=True, max_length=10)
    type_id = models.ForeignKey(verbose_name='Türü', null=True, blank=True, on_delete=(models.SET_NULL), to=OperationTypeModel,related_name="operation_info")
    detail = models.CharField(verbose_name='Detay', null=True, blank=True, max_length=200)
    datetime = models.DateTimeField(verbose_name='Zamanı', null=True, blank=True)
    user_id = models.ForeignKey(verbose_name='Sahibi', null=True, blank=True, on_delete=(models.SET_NULL), to=User,related_name="operation_info")
    branch_id = models.ForeignKey(verbose_name='Şube', on_delete=(models.CASCADE), to=BranchModel,default="",related_name="operation_info") 
    company_id = models.ForeignKey(verbose_name='Firma', null=True, blank=True,on_delete=(models.CASCADE), to=CompanyModel,default="",related_name="operation_info")
    objects = CustomManager()

    class Meta:
        db_table = 'authentication_operationhistory'
        ordering = []
        verbose_name = 'İşlem Geçmişi'

    def __str__(self):
        return '[%s] (%s) %s > %s : %s' % (self.datetime.strftime('%Y-%m-%d %H:%M:%S'), str(self.type_id), str(self.table_id), self.pk, self.detail)


class UserIpModel(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='IP Adres', max_length=50, unique=True, null=True)
    is_active = models.BooleanField(verbose_name='Aktiflik', null=True, blank=True, default=True)
    permission = models.BooleanField(verbose_name='İzin Durumu', null=True, blank=True, default=False)
    auth_key = models.CharField(verbose_name='Yetki Anahtarı', max_length=200, unique=True, null=True)
    activation_date = models.DateTimeField(verbose_name='Aktivasyon Zamanı', null=True, blank=True)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)
    branch_id = models.ForeignKey(verbose_name='Şube', on_delete=(models.CASCADE), to=BranchModel,default="",related_name="userip_info") 
    company_id = models.ForeignKey(verbose_name='Firma', null=True, blank=True,on_delete=(models.CASCADE), to=CompanyModel,default="",related_name="userip_info")
    objects = CustomManager()

    class Meta:
        db_table = 'authentication_userip'
        ordering = []
        verbose_name = 'Kullanıcı Ipsi'

    def __str__(self):
        if self.activation_date:
            return '[%s] %s : %s' % (self.activation_date.strftime('%Y-%m-%d %H:%M:%S'), str(self.ip_address), str(self.permission))
        return '[%s] %s : %s' % ('', str(self.ip_address), str(self.permission))

    def get_auth_key(self):
        ip_list = self.ip_address.split('.')
        dt = datetime.now()
        auth_key_text = '%s_%s-%s-%s-%s' % (dt.strftime('%y-%M-%d %H:%m:%s'), ip_list[0], ip_list[1], ip_list[2], ip_list[3])
        auth_key = make_password(auth_key_text)
        return auth_key

    def save(self, *args, **kwargs):
        if self.auth_key == '':
            ip_list = self.ip_address.split('.')
            dt = datetime.now()
            auth_key_text = '%s_%s-%s-%s-%s' % (dt.strftime('%y-%M-%d %H:%m:%s'), ip_list[0], ip_list[1], ip_list[2], ip_list[3])
            self.auth_key = make_password(auth_key_text)
            self.activation_date = dt
        return (super().save)(*args, **kwargs)





class TablePermissionModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    table_id = models.ForeignKey(verbose_name='Tablo', null=True, blank=True, on_delete=(models.SET_NULL), to=TableModel,related_name="tablepermission_info")
    action = models.CharField(verbose_name='İşlem', null=True, blank=True, max_length=100)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'authentication_tablepermission'
        ordering = ['table_id', 'action']
        verbose_name = 'Tablo İzni'
        unique_together = ('table_id', 'action')

    def __str__(self):
        return '%s > %s' % (self.table_id, self.action)


class FieldPermissionModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    field_id = models.ForeignKey(verbose_name='Model Alanı', null=True, blank=False, on_delete=(models.SET_NULL), to=FieldModel,related_name="fieldpermission_info")
    action = models.CharField(verbose_name='İşlem', null=True, blank=True, max_length=100)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)
    class Meta:
        db_table = 'authentication_fieldpermission'
        ordering = ['field_id', 'action']
        verbose_name = 'Model Alanı İzni'
        unique_together = ('field_id', 'action')

    def __str__(self):
        return '%s > %s' % (self.field_id, self.action)


class ObjectPermissionModel(models.Model):
    name = models.CharField(verbose_name='Adı', null=True, blank=True, max_length=100)
    table_id = models.ForeignKey(verbose_name='Tablo', null=True, blank=False, on_delete=(models.SET_NULL), to=TableModel,related_name="objectpermission_info")
    primary_key = models.CharField(verbose_name='Birincil Anahtar', null=True, blank=True, max_length=10)
    action = models.CharField(verbose_name='İşlem', null=True, blank=True, max_length=100)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'authentication_objectpermission'
        ordering = ['table_id', 'primary_key', 'action']
        verbose_name = 'Tablo Öğesi İzni'
        unique_together = ('table_id', 'primary_key', 'action')

    def __str__(self):
        return '%s > %s > %s' % (self.table_id, self.primary_key, self.action)


class GroupTablePermissionModel(models.Model):
    group_id = models.ForeignKey(verbose_name='Grup', null=True, blank=False, on_delete=(models.SET_NULL), to=AuthenticationGroupModel,related_name="grouptablepermission_info")
    table_permission_id = models.ForeignKey(verbose_name='Tablo Yetkisi', null=True, blank=False, on_delete=(models.SET_NULL), to=TablePermissionModel,related_name="grouptablepermission_info")
    permission = models.BooleanField(verbose_name='Yetki Durumu', default=False)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'authentication_grouptablepermission'
        ordering = ['table_permission_id', 'group_id']
        verbose_name = 'Tablo Yetkisi Olan Gruplar'
        unique_together = ('table_permission_id', 'group_id')

    def __str__(self):
        return '%s > %s' % (self.table_permission_id, self.group_id)


class GroupFieldPermissionModel(models.Model):
    group_id = models.ForeignKey(verbose_name='Grup', null=True, blank=False, on_delete=(models.SET_NULL), to=AuthenticationGroupModel,related_name="groupfieldpermission_info")
    field_permission_id = models.ForeignKey(verbose_name='Model Alanı Yetkisi', null=True, blank=False, on_delete=(models.SET_NULL), to=FieldPermissionModel,related_name="groupfieldpermission_info")
    permission = models.BooleanField(verbose_name='Yetki Durumu', default=False)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'authentication_groupfieldpermission'
        ordering = ['field_permission_id', 'group_id']
        verbose_name = 'Model Alanı Yetkisi Olan Gruplar'
        unique_together = ('field_permission_id', 'group_id')

    def __str__(self):
        return '%s > %s' % (self.field_permission_id, self.group_id)


class GroupObjectPermissionModel(models.Model):
    group_id = models.ForeignKey(verbose_name='Grup', null=True, blank=False, on_delete=(models.SET_NULL), to=AuthenticationGroupModel,related_name="groupobjectpermission_info")
    object_permission_id = models.ForeignKey(verbose_name='Tablo Objesi Yetkisi', null=True, blank=False, on_delete=(models.SET_NULL), to=ObjectPermissionModel,related_name="groupobjectpermission_info")
    permission = models.BooleanField(verbose_name='Yetki Durumu', default=False)
    desc = models.CharField(verbose_name='Açıklama', null=True, blank=True, max_length=500)

    class Meta:
        db_table = 'authentication_groupobjectpermission'
        ordering = ['object_permission_id', 'group_id']
        verbose_name = 'Tablo Öğesi Yetkisi Olan Gruplar'
        unique_together = ('object_permission_id', 'group_id')

    def __str__(self):
        return '%s > %s' % (self.object_permission_id, self.group_id)