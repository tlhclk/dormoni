# -*- coding: utf-8 -*-
### import_part
from calendarr.models import EventModel, NotificationModel
from calendarr.serializers import NotificationSerializer
from rest_framework import  viewsets
from rest_framework.response import Response
from datetime import datetime


### function_part

class GetNotifications(viewsets.ViewSet):
	def list(self, request):
		notification_queryset=NotificationModel.objects.all()
		next_events = EventModel.objects.filter(date__gte=datetime.today())
		serializer = NotificationSerializer(notification_queryset, many=True)
		# for event in next_events:
		# 	item=NotificationModel(title=self.name,content="%s > %s > %s > %s" % (str(event.type_id),str(event.date),str(event.time),event.location),is_active=True)
		# 	serializer.create(item)
		return Response(serializer.data)

