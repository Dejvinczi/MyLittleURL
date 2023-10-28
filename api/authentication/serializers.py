from rest_framework import serializers, exceptions

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(min_length=3, max_length=255)
    last_name = serializers.CharField(min_length=3, max_length=255)
    email = serializers.EmailField(min_length=6, max_length=255)
    password = serializers.CharField(write_only=True,
                                     min_length=8, max_length=64)

    class Meta:
        model = CustomUser
        fields = ['username', "first_name", "last_name", "email", "password"]

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(write_only=True,
                                     min_length=8, max_length=64, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', "password"]
