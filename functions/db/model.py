from django.apps import apps
from django.db.models import Q
import operator, datetime
AppModel = apps.get_model('schema', 'AppModel')
TableModel = apps.get_model('schema', 'TableModel')
FieldModel = apps.get_model('schema', 'FieldModel')
PathModel = apps.get_model('schema', 'PathModel')