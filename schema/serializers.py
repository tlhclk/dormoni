# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *
from parameters.serializers import AppTypeSerializer, PathTypeSerializer, FunctionTypeSerializer

class AppSerializer(serializers.ModelSerializer):
    type_id = AppTypeSerializer(many=False)
    str_output = serializers.SerializerMethodField()

    class Meta:
        model = AppModel
        fields = ['id', 'name', 'type_id', 'verbose_name', 'str_output']

    def get_str_output(self, obj):
        return '%s' % obj.verbose_name


class TableSerializer(serializers.ModelSerializer):
    app_id = AppSerializer(many=False)
    str_output = serializers.SerializerMethodField()

    class Meta:
        model = TableModel
        fields = ['id', 'name', 'db_table', 'verbose_name', 'list_title', 'form_title', 'detail_title', 'app_id', 'ordering', 'order', 'verbose_name_plural', 'str_output']

    def get_str_output(self, obj):
        return '%s > %s' % (obj.app_id, obj.verbose_name)


class FieldSerializer(serializers.ModelSerializer):
    table_id = TableSerializer(many=False)
    str_output = serializers.SerializerMethodField()

    class Meta:
        model = FieldModel
        fields = ['id', 'name', 'verbose_name', 'field', 'table_id', 'null', 'blank', 'max_length', 'on_delete', 'to', 'default', 'max_digits', 'decimal_places', 'is_generated', 'show_list', 'form_create', 'show_detail', 'form_update', 'form_delete', 'order', 'help_text', 'error_messages', 'auto_now', 'auto_now_add', 'str_output']

    def get_str_output(self, obj):
        return '%s > %s' % (obj.table_id, obj.verbose_name)


class PathSerializer(serializers.ModelSerializer):
    app_id = AppSerializer(many=False, read_only=True)
    type_id = PathTypeSerializer(many=False, read_only=True)
    str_output = serializers.SerializerMethodField()

    class Meta:
        model = PathModel
        fields = ['id', 'title', 'path', 'view_func', 'name', 'app_id', 'type_id', 'location', 'icon_code', 'str_output']

    def get_str_output(self, obj):
        return '%s > %s' % (obj.app_id, obj.title)


class FunctionSerializer(serializers.ModelSerializer):
    app_id = AppSerializer(many=False)
    type_id = FunctionTypeSerializer(many=False)
    str_output = serializers.SerializerMethodField()

    class Meta:
        model = FunctionModel
        fields = ['id', 'name', 'code', 'app_id', 'file_path', 'parent', 'order', 'type_id', 'data_path', 'str_output']

    def get_str_output(self, obj):
        return '%s > %s' % (obj.app_id, obj.name)