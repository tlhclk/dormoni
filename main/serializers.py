# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *
from parameters.serializers import MarketSerializer, CorporationTypeSerializer, CitySerializer, SchoolTypeSerializer, PeriodSerializer, TownSerializer

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = DepartmentModel
        fields = ['id', 'name', 'code']


class CorporationSerializer(serializers.ModelSerializer):
    market_id = MarketSerializer(many=False)
    type_id = CorporationTypeSerializer(many=False)
    city_id = CitySerializer(many=False)
    town_id = TownSerializer(many=False)

    class Meta:
        model = CorporationModel
        fields = ['id', 'name', 'market_id', 'type_id', 'city_id', 'town_id', 'hyperlink', 'address', 'phone_number']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeopleGroupModel
        fields = ['id', 'name', 'code']


class SchoolSerializer(serializers.ModelSerializer):
    type_id = SchoolTypeSerializer(many=False)
    city_id = CitySerializer(many=False)

    class Meta:
        model = SchoolModel
        fields = ['id', 'name', 'type_id', 'city_id']


class TaskSchedulerSerializer(serializers.ModelSerializer):
    period_id = PeriodSerializer(many=False)

    class Meta:
        model = TaskSchedulerModel
        fields = ['id', 'name', 'code', 'period_id', 'period_amount', 'run_time', 'run_func', 'is_active']