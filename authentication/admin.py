# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import CompanyModel, BranchModel
from .models import AuthenticationUserModel, AuthenticationGroupModel, UserGroupModel
admin.site.register(CompanyModel)
admin.site.register(BranchModel)
admin.site.register(AuthenticationUserModel)
admin.site.register(AuthenticationGroupModel)
admin.site.register(UserGroupModel)