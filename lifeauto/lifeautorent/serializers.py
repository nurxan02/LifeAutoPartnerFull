from rest_framework import serializers
from .models import EBike, Bike, Scooter, Car, Client, ClientDocument, ClientPayments, ClientPenalties

class EBikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EBike
        fields = '__all__'

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'

class ScooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scooter
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ClientDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientDocument
        fields = '__all__'

class ClientPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPayments
        fields = '__all__'

class ClientPenaltiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPenalties
        fields = '__all__'