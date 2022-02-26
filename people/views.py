from django.shortcuts import render
from functions.template.custom_view import CustomListView
from .models import PersonModel

# Create your views here.


class ListPerson(CustomListView):
	template_name = "people/list/person.html"
	model = PersonModel
	title = "Kişi Listesi"

