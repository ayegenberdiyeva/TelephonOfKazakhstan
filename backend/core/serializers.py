from rest_framework import serializers
from .models import User, TariffPlan, UserTariffPlan, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TariffPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffPlan
        fields = '__all__'

class UserTariffPlanSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tariff_plan = TariffPlanSerializer()

    class Meta:
        model = UserTariffPlan
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'