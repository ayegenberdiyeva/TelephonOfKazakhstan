from django.urls import path
from .views import (
    user_list,
    user_detail,
    tariff_plan_list,
    tariff_plan_detail,
    user_tariff_plan_list,
    user_tariff_plan_detail,
    all_tarif_plan_of_one_user,
    transaction_list,
    transaction_detail,
)

urlpatterns = [
    path('users/', user_list),
    path('users/<int:pk>/', user_detail),
    path('tariff-plans/', tariff_plan_list),
    path('tariff-plans/<int:pk>/', tariff_plan_detail),
    path('user-tariff-plans/', user_tariff_plan_list),
    path('user-tariff-plans/<int:pk>/', user_tariff_plan_detail),
    path('user/<int:pk>/tariff-plans/', all_tarif_plan_of_one_user),
    path('transactions/', transaction_list),
    path('transactions/<int:pk>/', transaction_detail),
]