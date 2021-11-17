# -*- coding: utf-8 -*-
from authentication.models import AuthenticationUserModel,AuthenticationGroupModel,UserGroupModel,TablePermissionModel,FieldPermissionModel,ObjectPermissionModel,UserTablePermissionModel,UserFieldPermissionModel,UserObjectPermissionModel,GroupTablePermissionModel,GroupFieldPermissionModel,GroupObjectPermissionModel
from functions.TableFuncs import ObjectFunc
from schema.models import TableModel,FieldModel

#get_permission(request,perm_type,action,**kwargs)
class Permission(ObjectFunc):
		
	def get_table_permission(self,table_id,action):
		pl=TablePermissionModel.object.filter(table_id=table_id,action=action)
		if len(pl)>0:
			if pl[0]:
				return pl[0]
		return None

	def get_field_permission(self,field_id,action):
		pl=FieldPermissionModel.object.filter(field_id=field_id,action=action)
		if len(pl)>0:
			if pl[0]:
				return pl[0]
		return None

	def get_object_permission(self,table_id,primary_key,action):
		pl=ObjectPermissionModel.object.filter(table_id=table_id,primary_key=primary_key,action=action)
		if len(pl)>0:
			if pl[0]:
				return pl[0]
		return None

	def check_group_table_permission(self,group_id,table_permission_id):
		gpl=GroupTablePermissionModel(group_id=group_id,table_permission_id=table_permission_id)
		if len(gpl)>0:
			if gpl[0].permission:
				return True
		return False

	def check_group_field_permission(self,group_id,field_permission_id):
		gpl=GroupFieldPermissionModel(group_id=group_id,field_permission_id=field_permission_id)
		if len(gpl)>0:
			if gpl[0].permission:
				return True
		return False

	def check_group_object_permission(self,group_id,object_permission_id):
		gpl=GroupObjectPermissionModel(group_id=group_id,object_permission_id=object_permission_id)
		if len(gpl)>0:
			if gpl[0].permission:
				return True
		return False

	def chect_user_table_permission(self,user_id,table_permission_id):
		upl=UserTablePermissionModel.objects.filter(user_id,table_permission_id)
		if len(upl)>0:
			if upl[0].permission:
				return True
		return False
		
	def chect_user_field_permission(self,user_id,field_permission_id):
		upl=UserFieldPermissionModel.objects.filter(user_id,field_permission_id)
		if len(upl)>0:
			if upl[0].permission:
				return True
		return False
		
	def chect_user_object_permission(self,user_id,object_permission_id):
		upl=UserObjectPermissionModel.objects.filter(user_id,object_permission_id)
		if len(upl)>0:
			if upl[0].permission:
				return True
		return False

	def get_groups(self,user_id):
		return [item.group_id for item in UserGroupModel.objects.filter(user_id)]

	def get_user(self,request):
		obj=AuthenticationUserModel.objects.get(user_id=request.user)
		return obj

	def get_permission(self,request,perm_type,action,**kwargs):
		user_id=self.get_user(request)
		if perm_type=="Table":
			if "table_name" in kwargs:
				table_obj=self.get_table_obj(kwargs["table_name"])
				if table_obj:
					pl=self.get_table_permission(table_obj,action)
					up=self.chect_user_table_permission(user_id,pl)
					if up:
						return True
					else:
						for group_id in self.get_groups(user_id):
							gp=self.check_group_table_permission(group_id,pl)
							if gp:
								return True
			return False
		elif perm_type == "Field":
			if "table_name" in kwargs and "field_name" in kwargs :
				field_obj=self.get_field_obj(kwargs["table_name"],kwargs["field_name"])
				if field_obj:
					pl=self.get_field_permission(field_obj,action)
					up=self.chect_user_field_permission(user_id,pl)
					if up:
						return True
					else:
						for group_id in self.get_groups(user_id):
							gp=self.check_group_field_permission(group_id,pl)
							if gp:
								return True
			return False
		elif perm_type == "Object":
			if "table_name" in kwargs and "primary_key" in kwargs :
				table_obj=self.get_table_obj(kwargs["table_name"])
				if table_obj:
					pl=self.get_object_permission(table_obj,kwargs["primary_key"],action)
					up=self.chect_user_object_permission(user_id,pl)
					if up:
						return True
					else:
						for group_id in self.get_groups(user_id):
							gp=self.check_group_object_permission(group_id,pl)
							if gp:
								return True
		else:
			return False




