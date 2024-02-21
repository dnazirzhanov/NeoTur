from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import User


class UserCreateSerializer(ModelSerializer):
    password = serializers.CharField(required=True, max_length=128, min_length=6, write_only=True)
    password_repeat = serializers.CharField(max_length=128, min_length=6, required=True, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password_repeat"]

    def validate(self, data):
        password = data.get('password')
        password_repeat = data.pop('password_repeat')
        if password != password_repeat:
            raise serializers.ValidationError({"error": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
