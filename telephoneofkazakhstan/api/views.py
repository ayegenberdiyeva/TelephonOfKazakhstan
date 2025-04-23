from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import TariffPlan, UserTariff, Transaction, User
from .serializers import TariffPlanSerializer, UserTariffSerializer, TransactionSerializer, UserSerializer, RegisterSerializer
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
import jwt
import datetime

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not user:
            raise NotAuthenticated("User is not authenticated")
        return Response({
            "name": user.name,
            "surname": user.surname,
            "phone_number": user.username,
            "tariff": {
                "name": user.tariff.name if user.tariff else None,
                "price": user.tariff.price if user.tariff else None,
                "data_limit": user.tariff.data_limit if user.tariff else None,
                "call_minutes": user.tariff.call_minutes if user.tariff else None,
                "sms_count": user.tariff.sms_count if user.tariff else None
            }
        })

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_tariff_plans(request):
    tariffs = TariffPlan.objects.all()
    serializer = TariffPlanSerializer(tariffs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        user = User.objects.filter(username=phone_number).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        payload = {
            'id': user.id,  # Use actual user ID
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
            'user_name': user.username
        }
        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated') 
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.get(id=payload['id'])
        serializer = UserSerializer(user)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_tariff(request):
    user = request.user
    name = request.data.get("name")

    if name in ["Basic", "Standard", "Premium"]:
        new_tariff = TariffPlan.objects.get(name=name)
    elif name == "mine":
        price = request.data.get("price")
        data_limit = request.data.get("data_limit")
        call_minutes = request.data.get("call_minutes")
        sms_count = request.data.get("sms_count")

        # Check if user already has a custom tariff
        existing_user_tariff = UserTariff.objects.filter(user=user, tariff__name=name).first()
        if existing_user_tariff:
            tariff = existing_user_tariff.tariff
            tariff.price = price
            tariff.data_limit = data_limit
            tariff.call_minutes = call_minutes
            tariff.sms_count = sms_count
            tariff.save()
            new_tariff = tariff
        else:
            new_tariff = TariffPlan.objects.create(
                name=f"custom_{user.id}",  # Unique name for custom tariff
                price=price,
                data_limit=data_limit,
                call_minutes=call_minutes,
                sms_count=sms_count
            )
            new_tariff.save()
            UserTariff.objects.create(user=user, tariff=new_tariff, is_active=True)
    else:
        return Response({"error": "Invalid tariff name"}, status=status.HTTP_400_BAD_REQUEST)

    # Update user's tariff
    UserTariff.objects.filter(user=user).update(is_active=False)
    UserTariff.objects.create(user=user, tariff=new_tariff, is_active=True)

    return Response({"message": f"Тариф успешно изменен на {new_tariff.name}"}, status=status.HTTP_200_OK)

class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_tariff = UserTariff.objects.filter(user=request.user, is_active=True).first()

        if not user_tariff:
            return Response({"error": "У вас нет активного тарифа"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": f"Оплата тарифа {user_tariff.tariff.name} прошла успешно!"}, status=status.HTTP_200_OK)