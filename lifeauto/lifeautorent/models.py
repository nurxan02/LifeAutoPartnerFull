from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator
from datetime import date
import uuid
from django.db.models import Sum


def generate_sku(prefix):
    unique_id = uuid.uuid4().hex[:8].upper()  
    return f"{prefix}-{unique_id}"

class EBike(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    battery_capacity = models.FloatField(help_text="Battery capacity in kWh")
    max_speed = models.FloatField(help_text="Maximum speed in km/h")
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True,verbose_name="Busy", help_text="Is the e-bike currently active?")
    image = models.ImageField(upload_to='ebikes/', null=True, blank=True, help_text="Upload an image of the e-bike")
    #Client
    client = models.ForeignKey(
        'Client',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='ebike',
        verbose_name="Client"
    )
    sku = models.CharField(max_length=50, unique=True, blank=True, verbose_name="SKU Code")
    def save(self, *args, **kwargs):
        if not self.sku:  
            self.sku = generate_sku("EB")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Bike(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    gear_count = models.IntegerField()
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True,verbose_name="Busy", help_text="Is the bike currently active?")
    image = models.ImageField(upload_to='bikes/', null=True, blank=True, help_text="Upload an image of the bike")
    #Client
    client = models.ForeignKey(
        'Client',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='bike',
        verbose_name="Client"
    )
    sku = models.CharField(max_length=50, unique=True, blank=True, verbose_name="SKU Code")
    def save(self, *args, **kwargs):
        if not self.sku:  
            self.sku = generate_sku("BI")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Scooter(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    max_speed = models.FloatField(help_text="Maximum speed in km/h")
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True,verbose_name="Busy", help_text="Is the scooter currently active?")
    image = models.ImageField(upload_to='scooters/', null=True, blank=True, help_text="Upload an image of the scooter")
    #Client
    client = models.ForeignKey(
        'Client',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='scooter',
        verbose_name="Client"
    )
    sku = models.CharField(max_length=50, unique=True, blank=True, verbose_name="SKU Code")
    def save(self, *args, **kwargs):
        if not self.sku:  
            self.sku = generate_sku("SC")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Car(models.Model):
    CATEGORY_CHOICES = [
        ('delivery', 'For Delivery'),
        ('taxi', 'For Taxi'),
    ]

    name = models.CharField(max_length=100, help_text="Name of the car model")
    brand = models.CharField(max_length=100, help_text="Name of the car brand")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name="Category", help_text="Category of the car: Delivery/Taxi")
    seating_capacity = models.IntegerField(help_text="Number of seats")
    price_per_week = models.DecimalField(max_digits=10, decimal_places=2, help_text="Weekly rental price")
    is_active = models.BooleanField(default=True, verbose_name="Busy", help_text="Is the car currently busy?")
    image = models.ImageField(upload_to='cars/', null=True, blank=True, help_text="Upload an image of the car")
    #Client
    client = models.ForeignKey(
        'Client',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='car',
        verbose_name="Client",
        help_text="Client who rented the car"
    )
    taxi_license_number = models.CharField(max_length=100, default="N/A", null=False, verbose_name="Taxi License Number",help_text="Taxi License number of the car")
    sign_number = models.CharField(max_length=100, null=False, verbose_name="Sign Number",help_text="Sign Number of the car")
    sku = models.CharField(max_length=50, unique=True, blank=True, verbose_name="SKU Code", help_text="Unique SKU code for the car")
    def save(self, *args, **kwargs):
        if not self.client:
            self.is_active = False
        if self.sign_number:
            self.sign_number = self.sign_number.upper()
        if not self.sku:  
            self.sku = f"C-{self.sign_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Client(models.Model):
    NATIONALITY_CHOICES = [
        # Priority countries
        ("Polish", "Polish"),
        ("Azerbaijani", "Azerbaijani"),
        ("Belarusian", "Belarusian"),
        ("Ukrainian", "Ukrainian"),
        ("Turkish", "Turkish"),
        # Other countries
        ("Afghan", "Afghan"),
        ("Albanian", "Albanian"),
        ("Algerian", "Algerian"),
        ("American", "American"),
        ("Andorran", "Andorran"),
        ("Angolan", "Angolan"),
        ("Antiguan", "Antiguan"),
        ("Argentine", "Argentine"),
        ("Armenian", "Armenian"),
        ("Australian", "Australian"),
        ("Austrian", "Austrian"),
        ("Bahamian", "Bahamian"),
        ("Bahraini", "Bahraini"),
        ("Bangladeshi", "Bangladeshi"),
        ("Barbadian", "Barbadian"),
        ("Belgian", "Belgian"),
        ("Belizean", "Belizean"),
        ("Beninese", "Beninese"),
        ("Bhutanese", "Bhutanese"),
        ("Bolivian", "Bolivian"),
        ("Bosnian", "Bosnian"),
        ("Botswanan", "Botswanan"),
        ("Brazilian", "Brazilian"),
        ("British", "British"),
        ("Bruneian", "Bruneian"),
        ("Bulgarian", "Bulgarian"),
        ("Burkinabe", "Burkinabe"),
        ("Burmese", "Burmese"),
        ("Burundian", "Burundian"),
        ("Cambodian", "Cambodian"),
        ("Cameroonian", "Cameroonian"),
        ("Canadian", "Canadian"),
        ("Cape Verdean", "Cape Verdean"),
        ("Central African", "Central African"),
        ("Chadian", "Chadian"),
        ("Chilean", "Chilean"),
        ("Chinese", "Chinese"),
        ("Colombian", "Colombian"),
        ("Comoran", "Comoran"),
        ("Congolese", "Congolese"),
        ("Costa Rican", "Costa Rican"),
        ("Croatian", "Croatian"),
        ("Cuban", "Cuban"),
        ("Cypriot", "Cypriot"),
        ("Czech", "Czech"),
        ("Danish", "Danish"),
        ("Djiboutian", "Djiboutian"),
        ("Dominican", "Dominican"),
        ("Dutch", "Dutch"),
        ("East Timorese", "East Timorese"),
        ("Ecuadorean", "Ecuadorean"),
        ("Egyptian", "Egyptian"),
        ("Emirati", "Emirati"),
        ("Equatorial Guinean", "Equatorial Guinean"),
        ("Eritrean", "Eritrean"),
        ("Estonian", "Estonian"),
        ("Ethiopian", "Ethiopian"),
        ("Fijian", "Fijian"),
        ("Finnish", "Finnish"),
        ("French", "French"),
        ("Gabonese", "Gabonese"),
        ("Gambian", "Gambian"),
        ("Georgian", "Georgian"),
        ("German", "German"),
        ("Ghanaian", "Ghanaian"),
        ("Greek", "Greek"),
        ("Grenadian", "Grenadian"),
        ("Guatemalan", "Guatemalan"),
        ("Guinea-Bissauan", "Guinea-Bissauan"),
        ("Guinean", "Guinean"),
        ("Guyanese", "Guyanese"),
        ("Haitian", "Haitian"),
        ("Honduran", "Honduran"),
        ("Hungarian", "Hungarian"),
        ("Icelandic", "Icelandic"),
        ("Indian", "Indian"),
        ("Indonesian", "Indonesian"),
        ("Iranian", "Iranian"),
        ("Iraqi", "Iraqi"),
        ("Irish", "Irish"),
        ("Israeli", "Israeli"),
        ("Italian", "Italian"),
        ("Ivorian", "Ivorian"),
        ("Jamaican", "Jamaican"),
        ("Japanese", "Japanese"),
        ("Jordanian", "Jordanian"),
        ("Kazakh", "Kazakh"),
        ("Kenyan", "Kenyan"),
        ("Kiribati", "Kiribati"),
        ("Kuwaiti", "Kuwaiti"),
        ("Kyrgyz", "Kyrgyz"),
        ("Laotian", "Laotian"),
        ("Latvian", "Latvian"),
        ("Lebanese", "Lebanese"),
        ("Liberian", "Liberian"),
        ("Libyan", "Libyan"),
        ("Liechtensteiner", "Liechtensteiner"),
        ("Lithuanian", "Lithuanian"),
        ("Luxembourgish", "Luxembourgish"),
        ("Macedonian", "Macedonian"),
        ("Malagasy", "Malagasy"),
        ("Malawian", "Malawian"),
        ("Malaysian", "Malaysian"),
        ("Maldivian", "Maldivian"),
        ("Malian", "Malian"),
        ("Maltese", "Maltese"),
        ("Marshallese", "Marshallese"),
        ("Mauritanian", "Mauritanian"),
        ("Mauritian", "Mauritian"),
        ("Mexican", "Mexican"),
        ("Micronesian", "Micronesian"),
        ("Moldovan", "Moldovan"),
        ("Monacan", "Monacan"),
        ("Mongolian", "Mongolian"),
        ("Montenegrin", "Montenegrin"),
        ("Moroccan", "Moroccan"),
        ("Mozambican", "Mozambican"),
        ("Namibian", "Namibian"),
        ("Nauruan", "Nauruan"),
        ("Nepalese", "Nepalese"),
        ("New Zealander", "New Zealander"),
        ("Nicaraguan", "Nicaraguan"),
        ("Nigerian", "Nigerian"),
        ("Nigerien", "Nigerien"),
        ("North Korean", "North Korean"),
        ("Norwegian", "Norwegian"),
        ("Omani", "Omani"),
        ("Pakistani", "Pakistani"),
        ("Palauan", "Palauan"),
        ("Panamanian", "Panamanian"),
        ("Papua New Guinean", "Papua New Guinean"),
        ("Paraguayan", "Paraguayan"),
        ("Peruvian", "Peruvian"),
        ("Philippine", "Philippine"),
        ("Polish", "Polish"),
        ("Portuguese", "Portuguese"),
        ("Qatari", "Qatari"),
        ("Romanian", "Romanian"),
        ("Russian", "Russian"),
        ("Rwandan", "Rwandan"),
        ("Saint Lucian", "Saint Lucian"),
        ("Salvadoran", "Salvadoran"),
        ("Samoan", "Samoan"),
        ("San Marinese", "San Marinese"),
        ("Sao Tomean", "Sao Tomean"),
        ("Saudi", "Saudi"),
        ("Senegalese", "Senegalese"),
        ("Serbian", "Serbian"),
        ("Seychellois", "Seychellois"),
        ("Sierra Leonean", "Sierra Leonean"),
        ("Singaporean", "Singaporean"),
        ("Slovak", "Slovak"),
        ("Slovenian", "Slovenian"),
        ("Solomon Islander", "Solomon Islander"),
        ("Somali", "Somali"),
        ("South African", "South African"),
        ("South Korean", "South Korean"),
        ("South Sudanese", "South Sudanese"),
        ("Spanish", "Spanish"),
        ("Sri Lankan", "Sri Lankan"),
        ("Sudanese", "Sudanese"),
        ("Surinamer", "Surinamer"),
        ("Swazi", "Swazi"),
        ("Swedish", "Swedish"),
        ("Swiss", "Swiss"),
        ("Syrian", "Syrian"),
        ("Taiwanese", "Taiwanese"),
        ("Tajik", "Tajik"),
        ("Tanzanian", "Tanzanian"),
        ("Thai", "Thai"),
        ("Togolese", "Togolese"),
        ("Tongan", "Tongan"),
        ("Trinidadian or Tobagonian", "Trinidadian or Tobagonian"),
        ("Tunisian", "Tunisian"),
        ("Turkish", "Turkish"),
        ("Turkmen", "Turkmen"),
        ("Tuvaluan", "Tuvaluan"),
        ("Ugandan", "Ugandan"),
        ("Ukrainian", "Ukrainian"),
        ("Uruguayan", "Uruguayan"),
        ("Uzbek", "Uzbek"),
        ("Vanuatuan", "Vanuatuan"),
        ("Venezuelan", "Venezuelan"),
        ("Vietnamese", "Vietnamese"),
        ("Yemeni", "Yemeni"),
        ("Zambian", "Zambian"),
        ("Zimbabwean", "Zimbabwean"),
        ("Not Specified", "Not Specified"),
    ]
       
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    date_of_birth = models.DateField(default=date(2000, 1, 1), verbose_name="Date of Birth")
    email = models.EmailField(unique=True,verbose_name="Email")
    country_code = models.CharField(max_length=10, verbose_name="Country Index", default="+48")
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number",   blank=True,
    null=True,    validators=[
        RegexValidator(
            regex=r'^\d{9,15}$',
            message="Phone number must contain only digits and be between 9 and 15 characters."
        )
    ])
    CHOICE_STATUS_CLIENT = (
    ('New', 'New'),
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
    ('Blocked', 'Blocked'),
    ('Deleted', 'Deleted'),
    )
    status = models.CharField(max_length=100, verbose_name="Status", choices=CHOICE_STATUS_CLIENT, default="New", null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, default="Not Specified", null=True, blank=True)
    address = models.TextField(blank=True, verbose_name="Address")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    is_contacted = models.BooleanField(default=False, verbose_name="Is Contacted")
    is_verified = models.BooleanField(default=False, verbose_name="Is Verified")
    
    def total_payments(self):
        total = self.Payments.filter(refundable=False).aggregate(Sum('payment_interests'))['payment_interests__sum']
        return total if total else 0 

    total_payments.short_description = "Total Payments" 
    def total_penalties(self):
        total = self.Penalties.aggregate(Sum('penalty_fee'))['penalty_fee__sum']
        return total if total else 0
    total_penalties.short_description = "Total Penalties"
    def rented_vehicles(self):
        vehicles = []
        if self.car.exists():
            vehicles.extend([f"Car: {car.brand} {car.name}-{car.sign_number}" for car in self.car.all()])
        if self.bike.exists():
            vehicles.extend([f"Bike: {bike.name}" for bike in self.bike.all()])
        if self.scooter.exists():
            vehicles.extend([f"Scooter: {scooter.name}" for scooter in self.scooter.all()])
        if self.ebike.exists():
            vehicles.extend([f"EBike: {ebike.name}" for ebike in self.ebike.all()])
        return ", ".join(vehicles) if vehicles else "No vehicles rented Right Now."
    rented_vehicles.short_description = "Rented Vehicles"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

def client_document_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{instance.client.first_name}_{instance.client.last_name}_{uuid.uuid4().hex[:4]}.{ext}"
    return f'rentalcarsclients/{instance.client.first_name}_{instance.client.last_name}/documents/{new_filename}'

class ClientDocument(models.Model):
    client = models.ForeignKey(
        'Client',
        on_delete=models.CASCADE,
        related_name='documents',
        verbose_name="Client"
    )
    document = models.FileField(
        upload_to=client_document_path,
        validators=[FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png'])],
        verbose_name="Document"
    )
    expire=models.BooleanField(default=False, verbose_name="Expire?")
    description = models.CharField(max_length=255, blank=True, verbose_name="Description")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded At")

    class Meta:
        verbose_name = "Client Document"
        verbose_name_plural = "Client Documents"

    def __str__(self):
        return f"Document for {self.client.first_name} {self.client.last_name}"
    
class ClientPayments(models.Model):
    client = models.ForeignKey('Client',on_delete=models.CASCADE, related_name='Payments',verbose_name="Client")
    description = models.CharField(max_length=255, blank=True, default="Weekly rental fee", verbose_name="Description")
    payment_interests= models.CharField(max_length=255, blank=True, verbose_name="Payment Interets")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    refundable = models.BooleanField(default=False, verbose_name="Refundable")

    class Meta:
        verbose_name = "Client Payment Interests"
        verbose_name_plural = "Client Payment Interests"
    def __str__(self):
        return f"Payment for {self.client.first_name} {self.client.last_name}"
    
class ClientPenalties(models.Model):
    client = models.ForeignKey('Client',on_delete=models.CASCADE, related_name='Penalties',verbose_name="Client")
    description = models.CharField(max_length=255, blank=True, verbose_name="Description")
    penalty_fee= models.CharField(max_length=255, blank=True, verbose_name="Penalty Interests")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Client Penalty"
        verbose_name_plural = "Client Penalties"
    def __str__(self):
        return f"Penalty for {self.client.first_name} {self.client.last_name}"