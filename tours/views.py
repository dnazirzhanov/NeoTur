from django.shortcuts import render
from django.utils import timezone
from .models import Tours, TourCategory, Recommendation
from .serializers import ToursSerializer, TourCategorySerializer, RecommendationSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class ToursCategoryAPIView(ListAPIView):
    queryset = TourCategory.objects.all()
    serializer_class = TourCategorySerializer


class ToursByCategoryAPIView(ListAPIView):
    serializer_class = ToursSerializer
    def get_queryset(self):
        category_id = self.kwargs['category_id']  # assuming you pass category_id in the URL
        return Tours.objects.filter(category__id=category_id)


class TourDetailView(RetrieveAPIView):
    queryset = Tours.objects.all()
    serializer_class = ToursSerializer

class RecommendedAPIView(ListAPIView):
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        current_month = timezone.now().month
        if current_month in [12, 1, 2]:  # Winter
            return Tours.objects.filter(Q(best_for_season='Winter') | Q(best_for_season='All Seasons'))
        elif current_month in [3, 4, 5]:  # Spring
            return Tours.objects.filter(Q(best_for_season='Spring') | Q(best_for_season='All Seasons'))
        elif current_month in [6, 7, 8]:  # Summer
            return Tours.objects.filter(Q(best_for_season='Summer') | Q(best_for_season='All Seasons'))
        elif current_month in [9, 10, 11]:  # Autumn
            return Tours.objects.filter(Q(best_for_season='Autumn') | Q(best_for_season='All Seasons'))
        else:
            return Tours.objects.none()

