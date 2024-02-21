from django.shortcuts import render
from .models import User
from .serializers import UserCreateSerializer, PhoneNumberSerializer
from rest_framework.generics import CreateAPIView


class CreateUsers(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer



