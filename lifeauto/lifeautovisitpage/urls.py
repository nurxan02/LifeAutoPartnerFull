from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ContactCreateView, BlogListView, BlogDetailView, ImportedVehicleAdvertisamentView, VehicleAdvertisementImageView, CustomerInquiryImportView,get_message_categories




urlpatterns = [
    path("contact/create/", ContactCreateView.as_view(), name="contact-create"),
    path("blogs/", BlogListView.as_view(), name='blog-list'),
    path("blogs/id=<int:pk>/", BlogDetailView.as_view(), name='blog-detail'),
    path("advertisements/", ImportedVehicleAdvertisamentView.as_view(), name="advertisement-list"),
    path("advertisement-images/", VehicleAdvertisementImageView.as_view(), name="advertisement-image-list"),
    path('message-categories/', get_message_categories, name='message_categories'),
    path("customer-inquiries/", CustomerInquiryImportView.as_view(), name="customer-inquiry-list"),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)