from django.db import models
from django.utils import timezone
from datetime import timedelta

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class TariffPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    data_limit = models.IntegerField()  # in MB
    call_minutes = models.IntegerField()  # in minutes
    sms_count = models.IntegerField()  # number of SMS
    description = models.TextField()
    duration = models.IntegerField()  # in days
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class UserTariffPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tariff_plan = models.ForeignKey(TariffPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = self.start_date + timedelta(days=self.tariff_plan.duration)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.tariff_plan.name}"

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.amount}"