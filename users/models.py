from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = PhoneNumberField()
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{self.username} - {self.first_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"