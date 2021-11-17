# -*- coding: utf-8 -*-
### import_part
from django.contrib import admin
from .models import NoteModel,NoteRecordModel


### admin_part
admin.site.register(NoteModel)
admin.site.register(NoteRecordModel)