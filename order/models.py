from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()



