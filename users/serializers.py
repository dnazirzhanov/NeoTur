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


class PhoneNumberSerializer(ModelSerializer):
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ["phone_number"]


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.pop('username', None)
        password = data.pop('password', None)

        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                data['user'] = user
            else:
                raise serializers.ValidationError("Пользователь с таким логином и паролем не найден.")
        else:
            raise serializers.ValidationError("Необходимо указать логин и пароль.")
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "email", "avatar", "birth_date", "phone_number"]