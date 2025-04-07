from rest_framework import generics
from .models import RegistrationPartner
from .serializers import RegistrationPartnerSerializer



class RegistrationPartnerCreateView(generics.CreateAPIView):
    queryset = RegistrationPartner.objects.all()
    serializer_class = RegistrationPartnerSerializer

class RegistrationPartnerListView(generics.ListAPIView):
    queryset = RegistrationPartner.objects.all()
    serializer_class = RegistrationPartnerSerializer