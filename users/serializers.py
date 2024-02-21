from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "password", "email", "first_name", "last_name", "phone_number"]
        extra_kwargs = {"password" : {"write_only" : True}}
