# -*- coding: utf-8 -*-
### import_part
from django.db import models
from schema.models import TableModel


### table_part
class NoteModel(models.Model):
	name = models.CharField(verbose_name='Adı',null=True,blank=True,max_length=100)
	note = models.CharField(verbose_name='Not',null=True,blank=True,max_length=50)
	desc = models.CharField(verbose_name='Açıklama',null=True,blank=True,max_length=500)
	code = models.CharField(verbose_name='Kodu',null=True,blank=True,max_length=20)

	class Meta:
		db_table='note_note'
		ordering=[]
		verbose_name='Not'

	def __str__(self):
		return "%s > %s > %s" % (self.name,str(self.note)[:50],str(self.desc)[:50])



### table_part
class NoteRecordModel(models.Model):
	table_id = models.ForeignKey(verbose_name='Tablo',null=True,blank=True,on_delete=models.SET_NULL,to=TableModel)
	primary_key = models.CharField(verbose_name='Birincil Anahtar',null=True,blank=True,max_length=10)
	note_id = models.ForeignKey(verbose_name='Not',null=True,blank=True,on_delete=models.SET_NULL,to=NoteModel)

	class Meta:
		db_table='note_noterecord'
		ordering=[]
		verbose_name='Not Kaydı'

	def __str__(self):
		return "%s > %s: %s" % (self.table_id,self.primary_key,self.note_id)

