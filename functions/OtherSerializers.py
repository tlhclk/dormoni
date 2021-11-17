from rest_framework import serializers

class NotificationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    datetime = serializers.CharField(max_length=100)
    hyperlink = serializers.CharField(max_length=100)
