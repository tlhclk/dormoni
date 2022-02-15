# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import PersonModel, EducationModel, EmailModel, PhoneModel, PhotoModel, SocialMediaModel, RelationshipModel, RelationshipPersonModel
admin.site.register(PersonModel)
admin.site.register(EducationModel)
admin.site.register(EmailModel)
admin.site.register(PhoneModel)
admin.site.register(PhotoModel)
admin.site.register(SocialMediaModel)
admin.site.register(RelationshipModel)
admin.site.register(RelationshipPersonModel)