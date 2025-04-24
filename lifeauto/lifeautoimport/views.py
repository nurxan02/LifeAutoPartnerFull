from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImportedCar, CarImage, CarDocument, Client
from .serializers import (
    ImportedCarSerializer, 
    CarImageSerializer, 
    CarDocumentSerializer, 
    ClientSerializer
)

class ClientAPIView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImportedCarAPIView(APIView):
    def get(self, request):
        cars = ImportedCar.objects.all()
        serializer = ImportedCarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImportedCarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarImageAPIView(APIView):
    def get(self, request):
        images = CarImage.objects.all()
        serializer = CarImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDocumentAPIView(APIView):
    def get(self, request):
        documents = CarDocument.objects.all()
        serializer = CarDocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)