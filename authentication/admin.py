# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import HistoryLogModel, OperationHistoryModel, UserIpModel
from .models import AuthenticationUserModel, AuthenticationGroupModel, UserGroupModel
from .models import TablePermissionModel, FieldPermissionModel, ObjectPermissionModel
from .models import UserTablePermissionModel, UserFieldPermissionModel, UserObjectPermissionModel
from .models import GroupTablePermissionModel, GroupFieldPermissionModel, GroupObjectPermissionModel
admin.site.register(HistoryLogModel)
admin.site.register(OperationHistoryModel)
admin.site.register(UserIpModel)
admin.site.register(AuthenticationUserModel)
admin.site.register(AuthenticationGroupModel)
admin.site.register(UserGroupModel)
admin.site.register(TablePermissionModel)
admin.site.register(FieldPermissionModel)
admin.site.register(ObjectPermissionModel)
admin.site.register(UserTablePermissionModel)
admin.site.register(UserFieldPermissionModel)
admin.site.register(UserObjectPermissionModel)
admin.site.register(GroupTablePermissionModel)
admin.site.register(GroupFieldPermissionModel)
admin.site.register(GroupObjectPermissionModel)