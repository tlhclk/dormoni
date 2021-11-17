# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import get_object_or_404
from note.models import NoteModel
import datetime



class NoteForm(forms.ModelForm):

	class Meta:
		model=NoteModel
		fields=['name','note','desc','code']

