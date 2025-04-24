from django.urls import path
from .views import (
    EBikeListAPIView, EBikeCreateAPIView,
    BikeListAPIView, BikeCreateAPIView,
    ScooterListAPIView, ScooterCreateAPIView,
    CarListAPIView, CarCreateAPIView,
    ClientListAPIView, ClientCreateAPIView,
    ClientDocumentListAPIView, ClientDocumentCreateAPIView,
    ClientPaymentsListAPIView, ClientPaymentsCreateAPIView,
    ClientPenaltiesListAPIView, ClientPenaltiesCreateAPIView
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
    path('clients/', ClientListAPIView.as_view(), name='client-list'),
    path('clients/create/', ClientCreateAPIView.as_view(), name='client-create'),
    path('client-documents/', ClientDocumentListAPIView.as_view(), name='client-document-list'),
    path('client-documents/create/', ClientDocumentCreateAPIView.as_view(), name='client-document-create'),
    path('client-payments/', ClientPaymentsListAPIView.as_view(), name='client-payments-list'),
    path('client-payments/create/', ClientPaymentsCreateAPIView.as_view(), name='client-payments-create'),
    path('client-penalties/', ClientPenaltiesListAPIView.as_view(), name='client-penalties-list'),
    path('client-penalties/create/', ClientPenaltiesCreateAPIView.as_view(), name='client-penalties-create'),
]