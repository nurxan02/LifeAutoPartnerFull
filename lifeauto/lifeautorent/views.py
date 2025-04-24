from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EBike, Bike, Scooter, Car, Client, ClientDocument, ClientPayments, ClientPenalties
from .serializers import EBikeSerializer, BikeSerializer, ScooterSerializer, CarSerializer, ClientSerializer, ClientDocumentSerializer, ClientPaymentsSerializer, ClientPenaltiesSerializer


class EBikeListAPIView(APIView):
    def get(self, request):
        ebikes = EBike.objects.all()
        serializer = EBikeSerializer(ebikes, many=True)
        return Response(serializer.data)

class EBikeCreateAPIView(APIView):
    def post(self, request):
        serializer = EBikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BikeListAPIView(APIView):
    def get(self, request):
        bikes = Bike.objects.all()
        serializer = BikeSerializer(bikes, many=True)
        return Response(serializer.data)

class BikeCreateAPIView(APIView):
    def post(self, request):
        serializer = BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScooterListAPIView(APIView):
    def get(self, request):
        scooters = Scooter.objects.all()
        serializer = ScooterSerializer(scooters, many=True)
        return Response(serializer.data)

class ScooterCreateAPIView(APIView):
    def post(self, request):
        serializer = ScooterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarListAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

class CarCreateAPIView(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientListAPIView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

class ClientCreateAPIView(APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDocumentListAPIView(APIView):
    def get(self, request):
        documents = ClientDocument.objects.all()
        serializer = ClientDocumentSerializer(documents, many=True)
        return Response(serializer.data)

class ClientDocumentCreateAPIView(APIView):
    def post(self, request):
        serializer = ClientDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientPaymentsListAPIView(APIView):
    def get(self, request):
        payments = ClientPayments.objects.all()
        serializer = ClientPaymentsSerializer(payments, many=True)
        return Response(serializer.data)

class ClientPaymentsCreateAPIView(APIView):
    def post(self, request):
        serializer = ClientPaymentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientPenaltiesListAPIView(APIView):
    def get(self, request):
        penalties = ClientPenalties.objects.all()
        serializer = ClientPenaltiesSerializer(penalties, many=True)
        return Response(serializer.data)

class ClientPenaltiesCreateAPIView(APIView):
    def post(self, request):
        serializer = ClientPenaltiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
