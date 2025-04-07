from rest_framework import serializers
from .models import EBike, Bike, Scooter, Car

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