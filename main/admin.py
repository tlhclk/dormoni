# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import DepartmentModel, CorporationModel, PeopleGroupModel, SchoolModel, TaskSchedulerModel
admin.site.register(DepartmentModel)
admin.site.register(CorporationModel)
admin.site.register(PeopleGroupModel)
admin.site.register(SchoolModel)
admin.site.register(TaskSchedulerModel)