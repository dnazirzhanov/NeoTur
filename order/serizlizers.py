from .models import Order
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from tours.models import Tours

class OrderSerializer(ModelSerializer):
    total_price = SerializerMethodField('get_total_price')

    class Meta:
        model = Order
        fields = ["user", "quantity"]

        def get_total_price(self, obj):
            tours = Tours.objects.filter(order=obj.id)
            total_price = 0
            for tour in tours:
                total_price += tour.price
            return total_price
