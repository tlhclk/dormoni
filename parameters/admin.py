# -*- coding: utf-8 -*-
from pathlib import Path
from django.contrib import admin
from .models import ContinentModel,CountryModel,CityModel,EmailTypeModel,GenderModel,MediaTypeModel,PhoneTypeModel,PeopleGroupModel,AppTypeModel,PathTypeModel


admin.site.register(ContinentModel)
admin.site.register(CountryModel)
admin.site.register(CityModel)
admin.site.register(EmailTypeModel)
admin.site.register(GenderModel)
admin.site.register(MediaTypeModel)
admin.site.register(PhoneTypeModel)
admin.site.register(PeopleGroupModel)
admin.site.register(AppTypeModel)
admin.site.register(PathTypeModel)
