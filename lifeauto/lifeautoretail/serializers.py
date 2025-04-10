from rest_framework import serializers
from .models import Car, CarImage, CustomerInquiry

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['id', 'image', 'is_primary']

class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)
    primary_image = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = [
            'id', 'brand', 'model', 'year', 'price', 'kilometer', 
            'color', 'body_type', 'engine_size', 'transmission',
            'fuel_type', 'horsepower', 'description', 'is_available',
            'created_at', 'updated_at', 'images', 'primary_image'
        ]
        read_only_fields = ('created_at', 'updated_at')

    def get_primary_image(self, obj):
        primary = obj.images.filter(is_primary=True).first()
        if primary:
            return CarImageSerializer(primary).data
        return None

class CustomerInquirySerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())
    car_details = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.DateTimeField(format="%d %b %Y %H:%M", read_only=True)

    class Meta:
        model = CustomerInquiry
        fields = [
            'id', 'car', 'car_details', 'name', 'email', 
            'phone', 'message', 'is_contacted', 'created_at'
        ]
        read_only_fields = ('created_at', 'is_contacted')

    def get_car_details(self, obj):
        return {
            'brand': obj.car.brand,  # Düzeltme: make yerine brand
            'model': obj.car.model,
            'year': obj.car.year,
            'price': obj.car.price
        }