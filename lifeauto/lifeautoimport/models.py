from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.core.validators import MinValueValidator
from decimal import Decimal
import os
import uuid

class ImportedCar(models.Model):
    # masin deyerler
    brand = models.CharField(max_length=100, verbose_name="Brand")
    model = models.CharField(max_length=100, verbose_name="Model")
    year = models.PositiveIntegerField(verbose_name="Year")
    vin = models.CharField(max_length=17, unique=True, verbose_name="VIN")
    kilometer = models.PositiveIntegerField(verbose_name="Kilometers")
    color = models.CharField(max_length=50, verbose_name="Color")
    fuel_type = models.CharField(max_length=20, choices=[
        ('gasoline', 'Gasoline'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
    ], verbose_name="Fuel Type")
    transmission = models.CharField(max_length=20, choices=[
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ], verbose_name="Transmission")
    engine_size = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Engine Size (L)")
    
    # auksion ve transport info
    auction_house = models.CharField(max_length=100, verbose_name="Auction House")
    auction_date = models.DateField(verbose_name="Auction Date")
    auction_location = models.CharField(max_length=100, verbose_name="Auction Location")
    auction_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Auction Price ($)")
    auction_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Auction Fee ($)")
    purchase_date = models.DateField(verbose_name="Purchase Date")
    
    # shipping info
    shipping_company = models.CharField(max_length=100, blank=True, verbose_name="Shipping Company")
    shipping_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Shipping Cost ($)")
    shipping_departure_date = models.DateField(blank=True, null=True, verbose_name="Shipping Departure Date")
    shipping_arrival_date = models.DateField(blank=True, null=True, verbose_name="Shipping Arrival Date")
    port_of_loading = models.CharField(max_length=100, blank=True, verbose_name="Port of Loading")
    port_of_discharge = models.CharField(max_length=100, blank=True, verbose_name="Port of Discharge")
    
    # sigorta
    insurance_company = models.CharField(max_length=100, blank=True, verbose_name="Insurance Company")
    insurance_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Insurance Cost ($)")
    insurance_policy_number = models.CharField(max_length=50, blank=True, verbose_name="Insurance Policy Number")
    
    # gomruk
    customs_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Customs Cost ($)")
    tax_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Tax Cost ($)")
    
    # son qiyamet
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Total Cost ($)")
    selling_price = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null=True, verbose_name="Selling Price ($)")

    # istatus
    STATUS_CHOICES = [
        ('auction', 'At Auction'),
        ('purchased', 'Purchased'),
        ('shipping', 'In Shipping'),
        ('customs', 'In Customs'),
        ('arrived', 'Arrived'),
        ('sold', 'Sold'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='auction', verbose_name="Status")
    
    # elave info
    notes = models.TextField(blank=True, verbose_name="Notes")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    def __str__(self):
        return f"{self.year} {self.brand} {self.model} ({self.vin})"
    
    #total cost'u otomatik  property
    @property
    def calculated_total_cost(self):
       
        costs = [
            self.auction_price or 0,
            self.auction_fee or 0,
            self.shipping_cost or 0,
            self.insurance_cost or 0,
            self.customs_cost or 0,
            self.tax_cost or 0
        ]
        return sum(costs)
    @property
    def net_profit(self):
        if self.selling_price and self.total_cost:
            return self.selling_price - self.total_cost
        return Decimal('0.00') 


    def save(self, *args, **kwargs):
        self.total_cost = self.calculated_total_cost

        if not self.selling_price or self.selling_price < self.total_cost:
            self.selling_price = round(self.total_cost * Decimal('1.20'), 2)
            
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Imported Car"
        verbose_name_plural = "Imported Cars"
        ordering = ['-auction_date']
        permissions = [
            ("view_net_profit", "Can view net profit"),
        ]

def car_image_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{instance.car.brand}+{instance.car.model}+{uuid.uuid4().hex[:4]}.{ext}"
    return f'importcars/{instance.car.vin}/images/{new_filename}'

def car_document_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{instance.car.brand}+{instance.car.model}+s{uuid.uuid4().hex[:4]}.{ext}"
    return f'importcars/{instance.car.vin}/documents/{new_filename}'

class CarImage(models.Model):
    car = models.ForeignKey(ImportedCar, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=car_image_path, verbose_name="Image")
    description = models.CharField(max_length=200, blank=True, verbose_name="Description")
    image_type = models.CharField(max_length=50, choices=[
        ('exterior', 'Exterior'),
        ('interior', 'Interior'),
        ('engine', 'Engine'),
        ('chassis', 'Chassis'),
        ('damage', 'Damage'),
        ('document', 'Document'),
        ('other', 'Other'),
    ], verbose_name="Image Type")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded At")
    
    class Meta:
        verbose_name = "Car Image"
        verbose_name_plural = "Car Images"


class CarDocument(models.Model):
    car = models.ForeignKey(ImportedCar, on_delete=models.CASCADE, related_name='documents')
    document = models.FileField(
        upload_to=car_document_path,
        validators=[FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png'])],
        verbose_name="Document"
    )
    document_type = models.CharField(max_length=50, choices=[
        ('auction', 'Auction Document'),
        ('invoice', 'Invoice'),
        ('bill_of_lading', 'Bill of Lading'),
        ('insurance', 'Insurance Document'),
        ('customs', 'Customs Document'),
        ('registration', 'Registration Document'),
        ('other', 'Other'),
    ], verbose_name="Document Type")
    description = models.CharField(max_length=200, blank=True, verbose_name="Description")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded At")
    
    class Meta:
        verbose_name = "Car Document"
        verbose_name_plural = "Car Documents"