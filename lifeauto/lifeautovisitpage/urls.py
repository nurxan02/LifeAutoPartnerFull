from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ContactCreateView, BlogListView, BlogDetailView




urlpatterns = [
    path("contact/create/", ContactCreateView.as_view(), name="contact-create"),
    path("blogs/", BlogListView.as_view(), name='blog-list'),
    path("blogs/id=<int:pk>/", BlogDetailView.as_view(), name='blog-detail'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)