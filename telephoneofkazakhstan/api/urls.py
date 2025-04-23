from django.urls import path
from .views import get_tariff_plans, change_tariff, PaymentView, RegisterView, LoginView, UserView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tariffs/', get_tariff_plans, name='get_tariff_plans'),
    path('change-tariff/', change_tariff, name='change_tariff'),
   # path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('register/', RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('profile/', ProfileView.as_view(), name='profile'),
    
]

