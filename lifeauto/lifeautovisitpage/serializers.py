from rest_framework import serializers
from .models import Blog, BlogImage, Contact, ImportedVehicleAdvertisament, VehicleAdvertisementImage, CustomerInquiryImport,AllCustomersCRM

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["name", "email", "tel", "message", "checkmark","message_category"]

class ImportedVehicleAdvertisamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportedVehicleAdvertisament
        fields = '__all__'

class VehicleAdvertisementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleAdvertisementImage
        fields = '__all__'
class CustomerInquiryImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInquiryImport
        fields = '__all__'
class AllCustomersCRMSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllCustomersCRM
        fields = '__all__'