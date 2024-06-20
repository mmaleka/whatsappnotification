# todo/todo_api/serializers.py
from rest_framework import serializers
from sendwhatsapp.models import WhatsAppNotification



class WhatsAppNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatsAppNotification
        fields = "__all__"
        