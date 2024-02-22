from django.db import models
from django.db.models import DateField
from order.models import Order


class TourCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tours(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    photo = models.ImageField()
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    best_for_season = models.CharField(max_length=20)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Recommendation(models.Model):
    current_time = models.DateField(auto_now_add=True)
    tours = models.OneToOneField(Tours, on_delete=models.CASCADE)

