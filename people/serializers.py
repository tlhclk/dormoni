# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *
from parameters.serializers import GenderSerializer, CountrySerializer, CitySerializer, SchoolTypeSerializer, EmailTypeSerializer, PhoneTypeSerializer, MediaTypeSerializer, RelationTypeSerializer
from main.serializers import GroupSerializer, SchoolSerializer, DepartmentSerializer

class PersonSerializer(serializers.ModelSerializer):
    gender_id = GenderSerializer(many=False)
    group_id = GroupSerializer(many=False)
    country_id = CountrySerializer(many=False)
    city_id = CitySerializer(many=False)

    class Meta:
        model = PersonModel
        fields = ['id', 'code', 'full_name', 'id_number', 'first_name', 'second_name', 'middle_name', 'last_name', 'nick_name', 'title', 'gender_id', 'group_id', 'date_of_birth', 'hometown', 'country_id', 'city_id', 'address', 'date_of_death', 'favorite']


class EducationSerializer(serializers.ModelSerializer):
    person_id = PersonSerializer(many=False)
    schooltype_id = SchoolTypeSerializer(many=False)
    school_id = SchoolSerializer(many=False)
    department_id = DepartmentSerializer(many=False)

    class Meta:
        model = EducationModel
        fields = ['id', 'person_id', 'schooltype_id', 'school_id', 'department_id', 'graduation_year']


class EmailSerializer(serializers.ModelSerializer):
    person_id = PersonSerializer(many=False)
    email_type_id = EmailTypeSerializer(many=False)

    class Meta:
        model = EmailModel
        fields = ['id', 'person_id', 'email_type_id', 'email']


class PhoneSerializer(serializers.ModelSerializer):
    person_id = PersonSerializer(many=False)
    phone_type_id = PhoneTypeSerializer(many=False)

    class Meta:
        model = PhoneModel
        fields = ['id', 'person_id', 'phone_type_id', 'phone_number']


class PhotoSerializer(serializers.ModelSerializer):
    person_id = PersonSerializer(many=False)

    class Meta:
        model = PhotoModel
        fields = ['id', 'person_id', 'name', 'hyperlink']


class SocialMediaSerializer(serializers.ModelSerializer):
    person_id = PersonSerializer(many=False)
    media_type_id = MediaTypeSerializer(many=False)

    class Meta:
        model = SocialMediaModel
        fields = ['id', 'person_id', 'media_type_id', 'username', 'hyperlink']


class RelationshipSerializer(serializers.ModelSerializer):
    person_id = PersonSerializer(many=False)
    relation_id = RelationTypeSerializer(many=False)

    class Meta:
        model = RelationshipModel
        fields = ['id', 'person_id', 'relation_id']


class RelationshipPersonSerializer(serializers.ModelSerializer):
    person_id = PersonSerializer(many=False)
    relation_tree_id = RelationshipSerializer(many=False)

    class Meta:
        model = RelationshipPersonModel
        fields = ['id', 'person_id', 'relation_tree_id']