from django.urls import path, include
from .views import CarsAPIView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('cars/', CarsAPIView.as_view()),
    path('cars/<int:pk>/', CarsAPIView.as_view()),
]