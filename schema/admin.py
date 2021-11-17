# -*- coding: utf-8 -*-
### import_part
from django.contrib import admin
from .models import AppModel,TableModel,FieldModel,PathModel


### admin_part
admin.site.register(AppModel)
admin.site.register(TableModel)
admin.site.register(FieldModel)
admin.site.register(PathModel)