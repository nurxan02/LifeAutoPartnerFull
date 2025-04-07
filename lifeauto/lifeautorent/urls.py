from django.urls import path
from .views import (
    EBikeListAPIView, EBikeCreateAPIView,
    BikeListAPIView, BikeCreateAPIView,
    ScooterListAPIView, ScooterCreateAPIView,
    CarListAPIView, CarCreateAPIView
)

urlpatterns = [
    path('ebikes/', EBikeListAPIView.as_view(), name='ebike-list'),  
    path('ebikes/create/', EBikeCreateAPIView.as_view(), name='ebike-create'), 
    path('bikes/', BikeListAPIView.as_view(), name='bike-list'),  
    path('bikes/create/', BikeCreateAPIView.as_view(), name='bike-create'), 
    path('scooters/', ScooterListAPIView.as_view(), name='scooter-list'), 
    path('scooters/create/', ScooterCreateAPIView.as_view(), name='scooter-create'),  
    path('cars/', CarListAPIView.as_view(), name='car-list'), 
    path('cars/create/', CarCreateAPIView.as_view(), name='car-create'),  
]