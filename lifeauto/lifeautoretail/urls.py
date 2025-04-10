from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    CarListView,
    CarDetailView,
    CarCreateView,
    CarImagesView,
    InquiryCreateView,
    InquiryListView,
    InquiryDetailView,
    CarInquiryCreateView,
)

urlpatterns = [
    path("cars/", CarListView.as_view(), name='car-list'),
    path("cars/create/", CarCreateView.as_view(), name='car-create'),
    path("cars/id=<int:pk>/", CarDetailView.as_view(), name='car-detail'),
    path("cars/id=<int:car_id>/images/", CarImagesView.as_view(), name='car-images'),
    path("inquiry/create/", InquiryCreateView.as_view(), name="inquiry-create"),
    path("inquiries/", InquiryListView.as_view(), name='inquiry-list'),
    path("inquiries/id=<int:pk>/", InquiryDetailView.as_view(), name='inquiry-detail'),
    path("cars/id=<int:car_id>/inquiry/", CarInquiryCreateView.as_view(), name='car-inquiry-create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)