from rest_framework import serializers
from .models import RegistrationPartner

class RegistrationPartnerSerializer(serializers.ModelSerializer):
    phone_number = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    
    class Meta:
        model = RegistrationPartner
        fields = [
            "first_name", "last_name", "email", "password",
            "phone_number", "nationality", "languages", "date_of_birth",
            "address", "has_bank_account", "bank_account_number",
            "is_student", "is_over_26", "has_company", "apps"
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_phone_number(self, obj):
        return {
            "country_code": obj.country_code,
            "number": obj.phone_number
        }

    def get_address(self, obj):
        return {
            "street": obj.street,
            "floor_number": obj.floor_number,
            "postcode": obj.postcode,
            "city": obj.city
        }

    def create(self, validated_data):

        request = self.context.get('request')
        phone_data = request.data.get('phoneNumber', {}) if request else {}
        address_data = request.data.get('address', {}) if request else {}
        

        registeredClient = RegistrationPartner.objects.create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            country_code=phone_data.get('countryCode'),
            phone_number=phone_data.get('number'),
            nationality=validated_data.get('nationality'),
            languages=validated_data.get('languages', []),
            date_of_birth=validated_data.get('date_of_birth'),
            street=address_data.get('street'),
            floor_number=address_data.get('floorNumber'),
            postcode=address_data.get('postcode'),
            city=address_data.get('city'),
            has_bank_account=validated_data.get('has_bank_account', False),
            bank_account_number=validated_data.get('bank_account_number'),
            is_student=validated_data.get('is_student', False),
            is_over_26=validated_data.get('is_over_26', False),
            has_company=validated_data.get('has_company', False),
            apps=validated_data.get('apps', [])
        )
        
        return registeredClient

    def to_internal_value(self, data):

        internal_value = super().to_internal_value(data)
        

        phone_data = data.get('phoneNumber', {})
        address_data = data.get('address', {})
        

        internal_value.update({
            'country_code': phone_data.get('countryCode'),
            'phone_number': phone_data.get('number'),
            'street': address_data.get('street'),
            'floor_number': address_data.get('floorNumber'),
            'postcode': address_data.get('postcode'),
            'city': address_data.get('city')
        })
        
        
        return internal_value
