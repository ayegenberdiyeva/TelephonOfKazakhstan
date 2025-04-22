from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import TariffPlan, UserTariff, Transaction, User
from .serializers import TariffPlanSerializer, UserTariffSerializer, TransactionSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from .serializers import RegisterSerializer

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "name": user.name,
            "surname": user.surname,
            "phone_number": user.username, 
            "tariff": user.tariff.name if hasattr(user, 'tariff') else None
        })

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        name = request.data.get("name")
        surname = request.data.get("surname")

        if not username or not password or not name or not surname:
            return Response({"error": "Username and password required"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(username=username, password=password, name = name, surname = surname )
        return Response({"message": "User created successfully"}, status=201)

@api_view(['GET'])
def get_tariff_plans(request):
    tariffs = TariffPlan.objects.all()
    serializer = TariffPlanSerializer(tariffs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        phone_number = request.data['phone_number']
        password = request.data['password']

        user = User.objects.filter(phone_number = phone_number).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        payload = {
            'id': 'user_id',
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes = 60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,'secret', algorithm='HS256').decode('utf-8')

        response = Response()
        response.set_cookies(key='jwt', value = token, httponly=True)
        response.data = {
            'jwt':token
        }
        return response
    

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated') 
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'] )

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.get(id = payload['id'])
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_tariff(request):
    user = request.user
    
    name = request.data.get("name")
    if name in ["Basic", "Standart", "Premium"]:
            new_tariff = TariffPlan.objects.get(name = name)
    elif name == "mine":

        price = request.data.get("price")
        data_limit = request.data.get("data_limit")
        call_minutss = request.data.get("call_minutes")
        sms_count = request.data.get("sms_count")

        if UserTariff.objects.filter(user = user and TariffPlan.objects.get(name = name)):
            UserTariff.objects.filter(user = user).update(price = price, data_limit = data_limit, call_minutss = call_minutss, sms_count = sms_count)
       
        new_tariff = TariffPlan.objects.create(name = "name", price = price, data_limit = data_limit, call_minutss = call_minutss, sms_count = sms_count)
        new_tariff.save()




    return Response({"message": f"Тариф успешно изменен на {new_tariff.name}"}, status=status.HTTP_200_OK)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)


class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_tariff = UserTariff.objects.filter(user=request.user, is_active=True).first()

        if not user_tariff:
            return Response({"error": "У вас нет активного тарифа"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": f"Оплата тарифа {user_tariff.tariff.name} прошла успешно!"}, status=status.HTTP_200_OK)
    

