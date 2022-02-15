# -*- coding: utf-8 -*-
from calendarr.models import EventModel, NotificationModel
from calendarr.serializers import NotificationSerializer
from .ReportFunc import GetReportData
from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime
from rest_framework.decorators import api_view

class GetNotifications(viewsets.ViewSet):

    def list(self, request):
        notification_queryset = NotificationModel.objects.all()
        next_events = EventModel.objects.filter(date__gte=(datetime.today()))
        serializer = NotificationSerializer(notification_queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_report_data(request):
    grd = GetReportData(request)
    data = grd.get_json_data()
    return Response(data)