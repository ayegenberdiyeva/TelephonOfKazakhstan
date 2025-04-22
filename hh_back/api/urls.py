from django.urls import path
from . import views
from .views import CompanyListView

urlpatterns = [
    path('companies/', CompanyListView.as_view()),
    path('vacancies/', views.vacancy_list),
    path('vacancies/top_ten/', views.top_ten_vacancies),
    path('vacancies/<int:id>/', views.vacancy_details),
    path('companies/<int:id>/', views.company_details),
    path('companies/<int:id>/vacancies/', views.company_vacancies)
]