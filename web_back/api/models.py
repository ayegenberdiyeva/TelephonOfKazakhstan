from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.TextField()
    surname = models.TextField()
    phone_number = models.TextField()
    password = models.TextField()
    is_Admin = models.TextField()

class TariffPlan(models.Model):
    name = models.TextField()
    price = models.FloatField()
    data_limit = models.FloatField()
    call_minutes = models.FloatField()
    sms_count = models.FloatField()

class UserTariff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tariff = models.ForeignKey(TariffPlan, ondelete = models.CASCADE)

