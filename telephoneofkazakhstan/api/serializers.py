from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, TariffPlan, UserTariff, Transaction
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'phone_number', 'password']

        extra_kwargs={
            'password':{'write_only': True}
        }
        
        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance


class TariffPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffPlan
        fields = '__all__'

class ChangeTariffSerializer(serializers.Serializer):
    new_tariff_id = serializers.IntegerField()
    
    def validate_new_tariff_id(self, value):
        if not TariffPlan.objects.filter(id=value).exists():
            raise serializers.ValidationError("Такого тарифного плана не существует.")
        return value

class PaymentSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    user_id = serializers.IntegerField()
    
    def validate(self, data):
        if data['amount'] <= 0:
            raise serializers.ValidationError("Сумма платежа должна быть положительной.")
        return data

class UserTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTariff
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'



class TariffPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffPlan
        fields = ['name', 'price', 'data_limit', 'call_minutes', 'sms_count']

class UserProfileSerializer(serializers.ModelSerializer):
    tariff = TariffPlanSerializer()

    class Meta:
        model = User
        fields = ['username', 'name', 'surname', 'tariff']
