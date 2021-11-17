# -*- coding: utf-8 -*-
### import_part
from django.contrib import admin
from .models import DepartmentModel,CorporationModel,PeopleGroupModel,SchoolModel,TaskSchedulerModel


### admin_part
admin.site.register(DepartmentModel)
admin.site.register(CorporationModel)
admin.site.register(PeopleGroupModel)
admin.site.register(SchoolModel)
admin.site.register(TaskSchedulerModel)