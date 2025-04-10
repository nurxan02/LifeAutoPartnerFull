from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Car(models.Model):
    BODY_TYPES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('hatchback', 'Hatchback'),
        ('coupe', 'Coupe'),
        ('convertible', 'Convertible'),
        ('pickup', 'Pickup'),
    ]
    
    TRANSMISSION_TYPES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
        ('semi-automatic', 'Semi-Automatic'),
    ]
    
    FUEL_TYPES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
        ('lpg', 'LPG'),
    ]
    
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2025)]
    )
    price = models.DecimalField(max_digits=12, decimal_places=2)
    kilometer = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    body_type = models.CharField(max_length=20, choices=BODY_TYPES)
    engine_size = models.DecimalField(max_digits=3, decimal_places=1)
    transmission = models.CharField(max_length=15, choices=TRANSMISSION_TYPES)
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPES)
    horsepower = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='car_images/')
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.car}"

class CustomerInquiry(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='inquiries')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    is_contacted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.car}"