from django.db import models

class RegistrationPartner(models.Model):
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
    ]
       
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    country_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)

    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES)
    languages = models.JSONField(blank=True, null=True)
    date_of_birth = models.DateField()

    street = models.CharField(max_length=255) 
    floor_number = models.CharField(max_length=20, blank=True, null=True)  
    postcode = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

    has_bank_account = models.BooleanField()
    bank_account_number = models.CharField(max_length=34, blank=True, null=True)

    is_student = models.BooleanField()
    is_over_26 = models.BooleanField()
    has_company = models.BooleanField()

    apps = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

class PartnerCarsList(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    sign_number = models.CharField(max_length=20)
    vin = models.CharField(max_length=17, unique=True)
    owner = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True )
    STATUS_CHOICES = [        
        ("Active", "Active"),
        ("Deactive", "Deactive"),
        ("Pending", "Pending"),
        ("Expired", "Expired"),
        ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name="License Status")

    def __str__(self):
        return f"{self.brand} {self.model} - ({self.sign_number})"
    
class PartnerCarsLicenses(models.Model):
    partner_car = models.ForeignKey(PartnerCarsList, on_delete=models.CASCADE)
    CITY_CHOICES = [
    # Masovian Voivodeship (Mazowieckie)
    ("Warsaw - Masovian", "Warsaw - Masovian"),
    ("Krakow - Lesser Poland", "Krakow - Lesser Poland"),
    # Silesian Voivodeship (Śląskie)
    ("Katowice - Silesian", "Katowice - Silesian"),
    ("Gliwice - Silesian", "Gliwice - Silesian"),
    ("Zabrze - Silesian", "Zabrze - Silesian"),
    ("Bytom - Silesian", "Bytom - Silesian"),
    ("Ruda Śląska - Silesian", "Ruda Śląska - Silesian"),
    ("Tychy - Silesian", "Tychy - Silesian"),
    ("Dąbrowa Górnicza - Silesian", "Dąbrowa Górnicza - Silesian"),
    ("Chorzów - Silesian", "Chorzów - Silesian"),
    ("Sosnowiec - Silesian", "Sosnowiec - Silesian"),
    ("Częstochowa - Silesian", "Częstochowa - Silesian"),
    ("Bielsko-Biała - Silesian", "Bielsko-Biała - Silesian"),
    ]
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    STATUS_CHOICES = [
        ("Licensed", "Licensed"),
        ("Unlicensed", "Unlicensed"),
        ("Pending", "Pending"),
        ("Expired", "Expired"),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city} - {self.status}"