# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *

class ContinentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContinentModel
        fields = ['id', 'name', 'code']


class CountrySerializer(serializers.ModelSerializer):
    continent_id = ContinentSerializer(many=False)

    class Meta:
        model = CountryModel
        fields = ['id', 'name', 'code', 'continent_id']


class CitySerializer(serializers.ModelSerializer):
    country_id = CountrySerializer(many=False)

    class Meta:
        model = CityModel
        fields = ['id', 'name', 'code', 'country_id']


class TownSerializer(serializers.ModelSerializer):
    city_id = CitySerializer(many=False)

    class Meta:
        model = TownModel
        fields = ['id', 'name', 'code', 'city_id']


class CardTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardTypeModel
        fields = ['id', 'name', 'code']


class ChangePurposeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChangePurposeModel
        fields = ['id', 'name', 'code']


class RepetitiveTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepetitiveTypeModel
        fields = ['id', 'name', 'code']


class CorporationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CorporationTypeModel
        fields = ['id', 'name', 'code']


class MarketSerializer(serializers.ModelSerializer):

    class Meta:
        model = MarketModel
        fields = ['id', 'name', 'code']


class EmailTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmailTypeModel
        fields = ['id', 'name', 'code']


class EventTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventTypeModel
        fields = ['id', 'name', 'code']


class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenderModel
        fields = ['id', 'name', 'code']


class MediaTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaTypeModel
        fields = ['id', 'name', 'base_url', 'code']


class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeriodModel
        fields = ['id', 'name', 'day', 'code']


class PhoneTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhoneTypeModel
        fields = ['id', 'name', 'code']


class RelationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelationTypeModel
        fields = ['id', 'name', 'code']


class SchoolTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolTypeModel
        fields = ['id', 'name', 'code']


class SeriesDownloadSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeriesDownloadModel
        fields = ['id', 'name', 'code']


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenreModel
        fields = ['id', 'name', 'code']


class SeriesStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeriesStateModel
        fields = ['id', 'name', 'code']


class SeriesTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeriesTypeModel
        fields = ['id', 'name', 'code']


class FinancialCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FinancialCategoryModel
        fields = ['id', 'name', 'code']


class TransactionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionTypeModel
        fields = ['id', 'name', 'code']


class OperationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperationTypeModel
        fields = ['id', 'name', 'code']


class AppTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppTypeModel
        fields = ['id', 'name', 'code']


class PathTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PathTypeModel
        fields = ['id', 'name', 'code', 'icon_code']


class ClothesTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothesTypeModel
        fields = ['id', 'name', 'code']


class CarClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarClassModel
        fields = ['id', 'name', 'code']


class CarTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarTypeModel
        fields = ['id', 'name', 'code']


class CarFuelTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarFuelTypeModel
        fields = ['id', 'name', 'code']


class CarUsageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarUsageModel
        fields = ['id', 'name', 'code']


class FunctionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FunctionTypeModel
        fields = ['id', 'name', 'code']