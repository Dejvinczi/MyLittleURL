from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions

from api.helpers.serializers import CustomDateTimeField

from .models import LittleURL


class LittleURLSerializer(serializers.ModelSerializer):
    raw_url = serializers.URLField(allow_blank=False)
    little_url = serializers.CharField(required=False)
    created_dt = CustomDateTimeField(required=False, read_only=True)
    owner = serializers.SlugRelatedField(slug_field='username', queryset=get_user_model(), required=False)

    def validate_little_url(self, little_url):
        '''
        Custom validation for raise ValidationError from rest_framework - not IntegrityError.
        '''
        if self.Meta.model.objects.filter(little_url=little_url):
            raise exceptions.ValidationError({'little_url': 'Little url is not available.'})

        return little_url

    class Meta:
        model = LittleURL
        fields = ("raw_url", "little_url", "created_dt", "owner")
