from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('order.urls')),
    path('', include('tours.urls')),
]
