# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import CompanyModel, BranchModel
from .models import PersonModel, EmailModel, PhoneModel,PhotoModel,SocialMediaModel

admin.site.register(PersonModel)
admin.site.register(EmailModel)
admin.site.register(PhoneModel)
admin.site.register(PhotoModel)
admin.site.register(SocialMediaModel)