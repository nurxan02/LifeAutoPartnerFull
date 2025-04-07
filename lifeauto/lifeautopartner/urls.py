from django.urls import path
from .views import RegistrationPartnerCreateView,RegistrationPartnerListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("RegistrationPartner/", RegistrationPartnerListView.as_view(), name="RegistrationPartner-list"),
    path("RegistrationPartner/create/", RegistrationPartnerCreateView.as_view(), name="RegistrationPartner-create"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)