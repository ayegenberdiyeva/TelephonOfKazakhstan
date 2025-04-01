from django.shortcuts import render
from .models import User, TariffPlan, UserTariffPlan, Transaction
from .serializers import UserSerializer, TariffPlanSerializer, UserTariffPlanSerializer, TransactionSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TariffPlanViewSet(viewsets.ModelViewSet):
    queryset = TariffPlan.objects.all()
    serializer_class = TariffPlanSerializer

class UserTariffPlanViewSet(viewsets.ModelViewSet):
    queryset = UserTariffPlan.objects.all()
    serializer_class = UserTariffPlanSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
