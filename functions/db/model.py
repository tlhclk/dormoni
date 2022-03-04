from django.apps import apps
from django.db.models import Q
import operator, datetime
AppModel = apps.get_model('schema', 'AppModel')
TableModel = apps.get_model('schema', 'TableModel')
FieldModel = apps.get_model('schema', 'FieldModel')
PathModel = apps.get_model('schema', 'PathModel')



class ObjectFunc:
    def __init__(self,table_name=None):
        self.table_name=table_name
        if table_name:
            self.table_obj=self.get_table_obj(table_name)
            self.table_model = self.get_table_model(self.table_obj)
        else:
            self.table_model=None
    
    def get_app(self,app_name):
        app_list=AppModel.objects.filter(name=app_name)
        if len(app_list)==1:
            return app_list[0]
        else:
            return None
    
    def get_table_obj(self):
        table_list=TableModel.objects.filter(name=self.table_name)
        if len(table_list)==1:
            return table_list[0]
        else:
            return None
    
    def get_table_model(self):
        return apps.get_model(self.table_obj.app_id.name, self.table_obj.name)
        
    def get_field_obj(self,field_name):
        field_list=FieldModel.objects.filter(table_id=self.table_obj).filter(name=field_name)
        if len(field_list)==1:
            return field_list[0]
        else:
            return None
    
    def get_field_list(self,purpose):
        if purpose == 'all':
            field_list = FieldModel.objects.filter(table_id=self.table_obj)
        elif purpose == 'show_list':
            field_list = FieldModel.objects.filter(table_id=self.table_obj).filter(show_list=True)
        elif purpose == 'show_detail':
            field_list = FieldModel.objects.filter(table_id=self.table_obj).filter(show_detail=True)
        elif purpose == 'form_create':
            field_list = FieldModel.objects.filter(table_id=self.table_obj).filter(form_create=True)
        elif purpose == 'form_update':
            field_list = FieldModel.objects.filter(table_id=self.table_obj).filter(form_update=True)
        elif purpose == 'form_delete':
            field_list = FieldModel.objects.filter(table_id=self.table_obj).filter(form_delete=True)
        else:
            field_list = []
        return field_list

class AttrDict(ObjectFunc):
    def __init__(self, object):
        super(AttrDict, self).__init__()
        self.table_name = object.__class__.__name__
        self.object = object
        if self.table_name:
            self.table_obj=self.get_table_obj(self.table_name)
            self.table_model = self.get_table_model(self.table_obj)
        else:
            self.table_model=None
    
    def get_attr_dict(self,purpose="All"):
        attr_dict = {}
        for field in self.get_field_list(purpose):
            attr_dict[field.name] = getattr(self.object, field.name)
        else:
            return attr_dict

    def get_remote_attr_dict(self,purpose="All"):
        remote_attr_dict = {}
        if purpose=="All":
            for field in FieldModel.objects.filter(to=(self.table_obj.name)):
                remote_attr_dict[field.table_id.name.lower().replace("model","")+"_info"] = [value for value in getattr(self.object, field.table_id.name.lower().replace("model","")+"_info").all()][:10]
        else:
            for field in FieldModel.objects.filter(to=(self.table_obj.name)).filter(Q(purpose,True)):
                remote_attr_dict[field.table_id.name.lower().replace("model","")+"_info"] = [value for value in getattr(self.object, field.table_id.name.lower().replace("model","")+"_info").all()][:10]
        return remote_attr_dict
    
    def get_dict(self,purpose="All"):
        return self.get_attr_dict(purpose) | self.get_remote_attr_dict(purpose)
