from django.contrib.auth.models import AbstractUser
from django.db import models



class TariffPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    data_limit = models.PositiveIntegerField(null=True, blank=True)
    call_minutes = models.PositiveIntegerField(null=True, blank=True)
    sms_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True) 
    password = models.CharField(max_length=255) 
    tariff = models.ForeignKey(TariffPlan, on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'username'  

class UserTariff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tariff = models.ForeignKey(TariffPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def change_tariff(self, new_tariff):
        self.tariff = new_tariff
        self.save()

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    old_tariff = models.ForeignKey(TariffPlan, on_delete=models.SET_NULL, null=True, blank=True, related_name="old_tariff")
    new_tariff = models.ForeignKey(TariffPlan, on_delete=models.CASCADE, related_name="new_tariff")
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction: {self.user.username} switched to {self.new_tariff.name}"

