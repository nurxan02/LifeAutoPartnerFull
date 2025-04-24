from rest_framework import serializers
from .models import ImportedCar, CarImage, CarDocument, Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = '__all__'

class CarDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDocument
        fields = '__all__'

class ImportedCarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)
    documents = CarDocumentSerializer(many=True, read_only=True)
    client = ClientSerializer(read_only=True)
    
    class Meta:
        model = ImportedCar
        fields = '__all__'
        read_only_fields = ('total_cost', 'selling_price', 'created_at', 'updated_at')