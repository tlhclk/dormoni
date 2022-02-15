# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import AppModel, TableModel, FieldModel, PathModel, FunctionModel
admin.site.register(AppModel)
admin.site.register(TableModel)
admin.site.register(FieldModel)
admin.site.register(PathModel)
admin.site.register(FunctionModel)