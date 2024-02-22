from .models import Recommendation, Tours, TourCategory
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class ToursSerializer(ModelSerializer):
    class Meta:
        model = Tours
        fields = ["__all__"]


class TourCategorySerializer(ModelSerializer):
    class Meta:
        model = TourCategory
        fields = ["__all__"]


class RecommendationSerializer(ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ["__all__"]



