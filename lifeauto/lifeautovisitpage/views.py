from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
# from django.shortcuts import render
# from rest_framework import viewsets
from .models import Blog, Contact, ImportedVehicleAdvertisament, VehicleAdvertisementImage, CustomerInquiryImport,AllCustomersCRM
from .serializers import BlogSerializer, ContactSerializer, ImportedVehicleAdvertisamentSerializer, VehicleAdvertisementImageSerializer, CustomerInquiryImportSerializer,AllCustomersCRMSerializer
from django.http import JsonResponse


def get_message_categories(request):
    categories = dict(Contact.MESSAGE_CATEGORY_CHOICES)
    return JsonResponse(categories)
class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)  


class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.filter(active=True) 
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
class BlogDetailView(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)  
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

class ImportedVehicleAdvertisamentView(generics.ListCreateAPIView):
    queryset = ImportedVehicleAdvertisament.objects.all()
    serializer_class = ImportedVehicleAdvertisamentSerializer

class VehicleAdvertisementImageView(generics.ListCreateAPIView):
    queryset = VehicleAdvertisementImage.objects.all()
    serializer_class = VehicleAdvertisementImageSerializer

class CustomerInquiryImportView(generics.ListCreateAPIView):
    queryset = CustomerInquiryImport.objects.all()
    serializer_class = CustomerInquiryImportSerializer

class AllCustomersCRMView(generics.ListCreateAPIView):
    queryset = AllCustomersCRM.objects.all()
    serializer_class = AllCustomersCRMSerializer