# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import AppModel,TableModel,FieldModel,PathModel,SidebarModel


admin.site.register(AppModel)
admin.site.register(TableModel)
admin.site.register(FieldModel)
admin.site.register(PathModel)
admin.site.register(SidebarModel)