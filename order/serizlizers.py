from .models import Order
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

class OrderSerializer(ModelSerializer):
    total_price = SerializerMethodField('get_total_price')

    class Meta:
        model = Order
        fields = "__all__"


