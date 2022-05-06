from django.urls import path
from api.views import CompanyView



urlpatterns = {
    path('companies/', CompanyView.as_view(), name='companies'),
    path('companies/<int:id>/', CompanyView.as_view(), name='companies_proccess'),
}