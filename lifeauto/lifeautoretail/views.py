from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from .models import Car, CarImage, CustomerInquiry
from .serializers import CarSerializer, CarImageSerializer, CustomerInquirySerializer

class CarListView(APIView):
    def get(self, request):
        cars = Car.objects.filter(is_available=True)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

class CarDetailView(APIView):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

class CarCreateView(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            car = serializer.save()
            
  
            images_data = request.FILES.getlist('images')
            for i, image_data in enumerate(images_data):
                CarImage.objects.create(
                    car=car,
                    image=image_data,
                    is_primary=(i == 0)
                )
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarImagesView(APIView):
    def get(self, request, car_id):
        car = get_object_or_404(Car, pk=car_id)
        images = car.images.all()
        serializer = CarImageSerializer(images, many=True)
        return Response(serializer.data)

    def post(self, request, car_id):
        car = get_object_or_404(Car, pk=car_id)
        image_data = request.FILES.get('image')
        is_primary = request.data.get('is_primary', False)
        
        if not image_data:
            return Response(
                {'error': 'No image provided'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        

        if is_primary:
            car.images.filter(is_primary=True).update(is_primary=False)
        
        image = CarImage.objects.create(
            car=car,
            image=image_data,
            is_primary=is_primary
        )
        
        return Response(
            CarImageSerializer(image).data, 
            status=status.HTTP_201_CREATED
        )

class InquiryCreateView(generics.CreateAPIView):
    queryset = CustomerInquiry.objects.all()
    serializer_class = CustomerInquirySerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class InquiryListView(APIView):
    def get(self, request):
        inquiries = CustomerInquiry.objects.all()
        serializer = CustomerInquirySerializer(inquiries, many=True)
        return Response(serializer.data)

class InquiryDetailView(APIView):
    def get(self, request, pk):
        inquiry = get_object_or_404(CustomerInquiry, pk=pk)
        serializer = CustomerInquirySerializer(inquiry)
        return Response(serializer.data)
    

class CarInquiryCreateView(APIView):
    def post(self, request, car_id):
        car = get_object_or_404(Car, pk=car_id)
        request.data['car'] = car.id 
        
        serializer = CustomerInquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)