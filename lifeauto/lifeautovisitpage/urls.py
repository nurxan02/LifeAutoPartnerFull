from django.conf import settings
from django.conf.urls.static import static
# from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactCreateView, BlogListView, BlogDetailView


# router = DefaultRouter()
# router.register(r'blogs', BlogViewSet)
# router.register(r'blog-images', BlogImageViewSet)
# router.register(r'contacts', ContactViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),  # API rotalarını dahil edin
# ]


urlpatterns = [
    # path('api/', include(router.urls)),  # API rotalarını dahil edin

    path("contact/create/", ContactCreateView.as_view(), name="contact-create"),
    path("blogs/", BlogListView.as_view(), name='blog-list'),
    path("blogs/id=<int:pk>/", BlogDetailView.as_view(), name='blog-detail'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)