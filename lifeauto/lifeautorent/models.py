from django.db import models



class EBike(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    battery_capacity = models.FloatField(help_text="Battery capacity in kWh")
    max_speed = models.FloatField(help_text="Maximum speed in km/h")
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True, help_text="Is the e-bike currently active?")
    image = models.ImageField(upload_to='ebikes/', null=True, blank=True, help_text="Upload an image of the e-bike")

    def __str__(self):
        return self.name


class Bike(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    gear_count = models.IntegerField()
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True, help_text="Is the bike currently active?")
    image = models.ImageField(upload_to='bikes/', null=True, blank=True, help_text="Upload an image of the bike")

    def __str__(self):
        return self.name


class Scooter(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    max_speed = models.FloatField(help_text="Maximum speed in km/h")
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True, help_text="Is the scooter currently active?")
    image = models.ImageField(upload_to='scooters/', null=True, blank=True, help_text="Upload an image of the scooter")

    def __str__(self):
        return self.name


class Car(models.Model):
    CATEGORY_CHOICES = [
        ('delivery', 'For Delivery'),
        ('taxi', 'For Taxi'),
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    seating_capacity = models.IntegerField()
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True, help_text="Is the car currently active?")
    image = models.ImageField(upload_to='cars/', null=True, blank=True, help_text="Upload an image of the car")

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

