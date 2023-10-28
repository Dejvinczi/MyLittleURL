import pytz

from rest_framework import serializers

from api.settings import TIME_ZONE


class CustomDateTimeField(serializers.DateTimeField):
    def to_representation(self, instance):
        format = getattr(self, 'format', "%Y-%m-%d %H:%M")
        local_timezone = pytz.timezone(TIME_ZONE)
        return instance.astimezone(local_timezone).strftime(format) if instance else None
