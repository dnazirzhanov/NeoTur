from django.urls import path
from .views import ToursCategoryAPIView, ToursByCategoryAPIView, TourDetailView, RecommendedAPIView

urlpatterns = [
    path('api/tour-categories/', ToursCategoryAPIView.as_view(), name='tour-categories'),
    path('api/tours/<int:category_id>/', ToursByCategoryAPIView.as_view(), name='tours-by-category'),
    path('api/tours/<int:pk>/', TourDetailView.as_view(), name='tour-detail'),
    path('api/recommended/', RecommendedAPIView.as_view(), name='recommended'),
]
