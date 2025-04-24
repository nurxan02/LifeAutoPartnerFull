from django.urls import path
from .views import (
    ClientAPIView,
    ImportedCarAPIView,
    CarImageAPIView,
    CarDocumentAPIView
)

urlpatterns = [
    path('import-clients/', ClientAPIView.as_view(), name='client-api'),
    path('imported-cars/', ImportedCarAPIView.as_view(), name='imported-car-api'),
    path('imported-car-images/', CarImageAPIView.as_view(), name='car-image-api'),
    path('imported-car-documents/', CarDocumentAPIView.as_view(), name='car-document-api'),
]