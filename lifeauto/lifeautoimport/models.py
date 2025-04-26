from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from decimal import Decimal
import uuid
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import date
from django.core.validators import RegexValidator
from PIL import Image
import os
from django.core.files.base import ContentFile

class ImportedCar(models.Model):
    # masin deyerler
    CHOICE_CAR_BRANDS = [
    ('select', 'Select Brand'),
    ('Abarth', 'Abarth'),
    ('Acura', 'Acura'),
    ('Aiways', 'Aiways'),
    ('Alfa Romeo', 'Alfa Romeo'),
    ('Alpine', 'Alpine'),
    ('Aptera', 'Aptera'),
    ('Arcfox', 'Arcfox'),
    ('Ariel', 'Ariel'),
    ('Aston Martin', 'Aston Martin'),
    ('Audi', 'Audi'),
    ('Automobili Pininfarina', 'Automobili Pininfarina'),
    ('BAIC', 'BAIC'),
    ('Baojun', 'Baojun'),
    ('Bentley', 'Bentley'),
    ('Bestune', 'Bestune'),
    ('Bisu', 'Bisu'),
    ('BMW', 'BMW'),
    ('Bollinger', 'Bollinger'),
    ('Borgward', 'Borgward'),
    ('Brilliance Auto', 'Brilliance Auto'),
    ('Buick', 'Buick'),
    ('BYD', 'BYD'),
    ('Cadillac', 'Cadillac'),
    ('Canoo', 'Canoo'),
    ('Caparo', 'Caparo'),
    ('Changan', 'Changan'),
    ('Changfeng', 'Changfeng'),
    ('Chery', 'Chery'),
    ('Chevrolet', 'Chevrolet'),
    ('Chrysler', 'Chrysler'),
    ('Citroën', 'Citroën'),
    ('Cupra', 'Cupra'),
    ('Dacia', 'Dacia'),
    ('Daewoo', 'Daewoo'),
    ('Daihatsu', 'Daihatsu'),
    ('Datsun', 'Datsun'),
    ('De Tomaso', 'De Tomaso'),
    ('Denza', 'Denza'),
    ('Detroit Electric', 'Detroit Electric'),
    ('DFSK', 'DFSK'),
    ('Dodge', 'Dodge'),
    ('Dongfeng', 'Dongfeng'),
    ('DS Automobiles', 'DS Automobiles'),
    ('Eagle', 'Eagle'),
    ('FAW', 'FAW'),
    ('Ferrari', 'Ferrari'),
    ('Fiat', 'Fiat'),
    ('Fisker', 'Fisker'),
    ('Ford', 'Ford'),
    ('Foton', 'Foton'),
    ('Geely', 'Geely'),
    ('Genesis', 'Genesis'),
    ('GMC', 'GMC'),
    ('Great Wall Motors', 'Great Wall Motors'),
    ('Haima', 'Haima'),
    ('Haval', 'Haval'),
    ('Hawtai', 'Hawtai'),
    ('Hennessey', 'Hennessey'),
    ('HiPhi', 'HiPhi'),
    ('Honda', 'Honda'),
    ('Hongqi', 'Hongqi'),
    ('Hummer', 'Hummer'),
    ('Hyundai', 'Hyundai'),
    ('Ineos', 'Ineos'),
    ('Infiniti', 'Infiniti'),
    ('Iran Khodro', 'Iran Khodro'),
    ('Isuzu', 'Isuzu'),
    ('JAC', 'JAC'),
    ('Jaguar', 'Jaguar'),
    ('Jeep', 'Jeep'),
    ('JETTA', 'JETTA'),
    ('Jonway', 'Jonway'),
    ('Karma', 'Karma'),
    ('KGM (SsangYong)', 'KGM (SsangYong)'),
    ('Kia', 'Kia'),
    ('Koenigsegg', 'Koenigsegg'),
    ('Krajina', 'Krajina'),
    ('Lada', 'Lada'),
    ('Lamborghini', 'Lamborghini'),
    ('Lancia', 'Lancia'),
    ('Land Rover', 'Land Rover'),
    ('Leapmotor', 'Leapmotor'),
    ('Lexus', 'Lexus'),
    ('Li Auto', 'Li Auto'),
    ('Lifan', 'Lifan'),
    ('Lincoln', 'Lincoln'),
    ('Lotus', 'Lotus'),
    ('Lucid', 'Lucid'),
    ('Lynk & Co', 'Lynk & Co'),
    ('Mahindra', 'Mahindra'),
    ('Maserati', 'Maserati'),
    ('Maxus', 'Maxus'),
    ('Maybach', 'Maybach'),
    ('Mazda', 'Mazda'),
    ('McLaren', 'McLaren'),
    ('Mercedes-Benz', 'Mercedes-Benz'),
    ('MG', 'MG'),
    ('Mini', 'Mini'),
    ('Mitsubishi', 'Mitsubishi'),
    ('Morris Garages', 'Morris Garages'),
    ('NIO', 'NIO'),
    ('Nissan', 'Nissan'),
    ('Ora', 'Ora'),
    ('Opel', 'Opel'),
    ('Pagani', 'Pagani'),
    ('Peugeot', 'Peugeot'),
    ('Polestar', 'Polestar'),
    ('Pontiac', 'Pontiac'),
    ('Porsche', 'Porsche'),
    ('Proton', 'Proton'),
    ('Qoros', 'Qoros'),
    ('Ram', 'Ram'),
    ('Ravon', 'Ravon'),
    ('Renault', 'Renault'),
    ('Rimac', 'Rimac'),
    ('Roewe', 'Roewe'),
    ('Rolls-Royce', 'Rolls-Royce'),
    ('Rover', 'Rover'),
    ('Saab', 'Saab'),
    ('Saic MG', 'Saic MG'),
    ('Samsung Motors', 'Samsung Motors'),
    ('Seat', 'Seat'),
    ('Seres', 'Seres'),
    ('Shelby', 'Shelby'),
    ('Skoda', 'Škoda'),
    ('Smart', 'Smart'),
    ('Soueast', 'Soueast'),
    ('SsangYong', 'SsangYong'),
    ('Stellantis', 'Stellantis'), # Birleşmiş bir grup, tek marka olarak değerlendirilebilir.
    ('Subaru', 'Subaru'),
    ('Suzuki', 'Suzuki'),
    ('Tata', 'Tata'),
    ('Tatra', 'Tatra'),
    ('Tesla', 'Tesla'),
    ('Tianjin Xiali', 'Tianjin Xiali'),
    ('Toyota', 'Toyota'),
    ('Trabant', 'Trabant'),
    ('Triumph', 'Triumph'),
    ('TVR', 'TVR'),
    ('Vauxhall', 'Vauxhall'),
    ('Venucia', 'Venucia'),
    ('Volkswagen', 'Volkswagen'),
    ('Volvo', 'Volvo'),
    ('Weltmeister (WM Motor)', 'Weltmeister (WM Motor)'),
    ('Wuling', 'Wuling'),
    ('Xpeng', 'Xpeng'),
    ('Yugo', 'Yugo'),
    ('Zastava', 'Zastava'),
    ('Zotye', 'Zotye'),
    ('ZX Auto', 'ZX Auto'),
]
    brand = models.CharField(max_length=100, choices=CHOICE_CAR_BRANDS, default='select', verbose_name="Brand")
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
    CONDITION_TYPE_CHOICES = [
        ('clean_title', 'Clean Title'),     
        ('normal_wear', 'Normal Wear'),
        ('exceeds_mechanical_limits', 'Exceeds Mechanical Limits'),
        ('biohazard', 'Biohazard / Chemical'),
        ('burn_engine', 'Burn - Engine'),
        ('burn_interior', 'Burn - Interior'),
        ('burn_exterior', 'Burn - Exterior'),
        ('damage_history', 'Damage History'),
        ('frame_damage', 'Frame Damage'),
        ('hail_damage', 'Hail Damage'),
        ('mechanical', 'Mechanical'),
        ('mileage_discrepancy', 'Mileage Discrepancy'),
        ('partial_repair', 'Partial Repair'),
        ('rejected_repair', 'Rejected Repair'),
        ('rollover', 'Rollover'),
        ('side_damage', 'Side Damage'),
        ('stripped', 'Stripped'),
        ('theft_recovery', 'Theft Recovery'),
        ('undercarriage_damage', 'Undercarriage Damage'),
        ('vandalism', 'Vandalism'),
        ('water_flood', 'Water / Flood'),
        ('all_over_damage', 'All Over Damage'),
    ]

    condition_type = models.CharField(
        max_length=50,
        choices=CONDITION_TYPE_CHOICES,
        verbose_name="Vehicle Condition Type",
        
    )
    CHOICE_KEY_PROPERTY = [
        ('Has Key', 'Has Key'),
        ('Missing', 'Missing'),
        ('Other', 'Other'),
    ]
    key = models.CharField(max_length=50, choices=CHOICE_KEY_PROPERTY, blank=True, verbose_name="Key")
    
    # auksion ve transport info
    CHOICE_AUCTION_COUNTRY = [
        ('USA', 'USA'),
        ('Canada', 'Canada'),
        ('Germany', 'Germany'),
        ('France', 'France'),
        ('Italy', 'Italy'),
        ('Netherlands', 'Netherlands'),
        ('Belgium', 'Belgium'),
        ('United Kingdom', 'United Kingdom'),
        ('Turkey', 'Turkey'),
        ('United Arab Emirates', 'United Arab Emirates'),
        ('Japan', 'Japan'),
        ('South Korea', 'South Korea'),
        ('China', 'China'),
        ('Russia', 'Russia'),
        ('Spain', 'Spain'),
        ('Poland', 'Poland'),
        ('Georgia', 'Georgia'),
        ('Ukraine', 'Ukraine'),
    ]
    auction_country=models.CharField(choices=CHOICE_AUCTION_COUNTRY, max_length=50,  verbose_name="Auction Country")
    auction_house = models.CharField(max_length=100, verbose_name="Auction Company")
    auction_date = models.DateField(verbose_name="Auction Date")
    auction_location = models.CharField(max_length=100, verbose_name="Auction Location")
    auction_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Auction Price (zł)")
    auction_fee = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Auction Fee (zł)")
    purchase_date = models.DateField(verbose_name="Purchase Date")
    
    # shipping info
    shipping_company = models.CharField(max_length=100, blank=True, verbose_name="Shipping Company")
    shipping_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Shipping Cost (zł)")
    shipping_departure_date = models.DateField(blank=True, null=True, verbose_name="Shipping Departure Date")
    shipping_arrival_date = models.DateField(blank=True, null=True, verbose_name="Shipping Arrival Date")
    port_of_loading = models.CharField(max_length=100, blank=True, verbose_name="Port of Loading")
    port_of_discharge = models.CharField(max_length=100, blank=True, verbose_name="Port of Discharge")
    
    # sigorta
    insurance_company = models.CharField(max_length=100, blank=True, verbose_name="Insurance Company")
    insurance_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Insurance Cost (zł)")
    insurance_policy_number = models.CharField(max_length=50, blank=True, verbose_name="Insurance Policy Number")
    
    # gomruk
    customs_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Customs Cost (zł)")
    tax_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Tax Cost (zł)")
    
    # son qiyamet
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Total Cost (zł)")
    selling_price = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null=True, verbose_name="Selling Price (zł)")

    #Client
    client = models.ForeignKey(
        'Client',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cars',
        verbose_name="Client"
    )
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
    
    #total cost'u   property
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
        verbose_name = "Imported Car US"
        verbose_name_plural = "Imported Car US"
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

def advertisement_image_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{instance.id}_{uuid.uuid4().hex[:8]}.{ext}"
    return os.path.join('advertisements/', new_filename)

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
    def delete(self, *args, **kwargs):
        if self.image and os.path.exists(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)
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

    country_code = models.CharField(max_length=10, verbose_name="Country Index", default="+48", null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number",   blank=True,
    null=True,    validators=[
        RegexValidator(
            regex=r'^\d{9,15}$',
            message="Phone number must contain only digits and be between 9 and 15 characters."
        )
    ])
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, default="Not Specified", null=True, blank=True)
    address = models.TextField(blank=True, verbose_name="Address")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    is_verified = models.BooleanField(default=False, verbose_name="Is Verified")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
