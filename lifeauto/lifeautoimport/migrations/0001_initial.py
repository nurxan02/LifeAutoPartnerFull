# Generated by Django 5.2 on 2025-05-14 13:48

import datetime
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import lifeautoimport.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(default=datetime.date(2000, 1, 1), verbose_name='Date of Birth')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('country_code', models.CharField(blank=True, default='+48', max_length=10, null=True, verbose_name='Country Index')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must contain only digits and be between 9 and 15 characters.', regex='^\\d{9,15}$')], verbose_name='Phone Number')),
                ('nationality', models.CharField(blank=True, choices=[('Polish', 'Polish'), ('Azerbaijani', 'Azerbaijani'), ('Belarusian', 'Belarusian'), ('Ukrainian', 'Ukrainian'), ('Turkish', 'Turkish'), ('Afghan', 'Afghan'), ('Albanian', 'Albanian'), ('Algerian', 'Algerian'), ('American', 'American'), ('Andorran', 'Andorran'), ('Angolan', 'Angolan'), ('Antiguan', 'Antiguan'), ('Argentine', 'Argentine'), ('Armenian', 'Armenian'), ('Australian', 'Australian'), ('Austrian', 'Austrian'), ('Bahamian', 'Bahamian'), ('Bahraini', 'Bahraini'), ('Bangladeshi', 'Bangladeshi'), ('Barbadian', 'Barbadian'), ('Belgian', 'Belgian'), ('Belizean', 'Belizean'), ('Beninese', 'Beninese'), ('Bhutanese', 'Bhutanese'), ('Bolivian', 'Bolivian'), ('Bosnian', 'Bosnian'), ('Botswanan', 'Botswanan'), ('Brazilian', 'Brazilian'), ('British', 'British'), ('Bruneian', 'Bruneian'), ('Bulgarian', 'Bulgarian'), ('Burkinabe', 'Burkinabe'), ('Burmese', 'Burmese'), ('Burundian', 'Burundian'), ('Cambodian', 'Cambodian'), ('Cameroonian', 'Cameroonian'), ('Canadian', 'Canadian'), ('Cape Verdean', 'Cape Verdean'), ('Central African', 'Central African'), ('Chadian', 'Chadian'), ('Chilean', 'Chilean'), ('Chinese', 'Chinese'), ('Colombian', 'Colombian'), ('Comoran', 'Comoran'), ('Congolese', 'Congolese'), ('Costa Rican', 'Costa Rican'), ('Croatian', 'Croatian'), ('Cuban', 'Cuban'), ('Cypriot', 'Cypriot'), ('Czech', 'Czech'), ('Danish', 'Danish'), ('Djiboutian', 'Djiboutian'), ('Dominican', 'Dominican'), ('Dutch', 'Dutch'), ('East Timorese', 'East Timorese'), ('Ecuadorean', 'Ecuadorean'), ('Egyptian', 'Egyptian'), ('Emirati', 'Emirati'), ('Equatorial Guinean', 'Equatorial Guinean'), ('Eritrean', 'Eritrean'), ('Estonian', 'Estonian'), ('Ethiopian', 'Ethiopian'), ('Fijian', 'Fijian'), ('Finnish', 'Finnish'), ('French', 'French'), ('Gabonese', 'Gabonese'), ('Gambian', 'Gambian'), ('Georgian', 'Georgian'), ('German', 'German'), ('Ghanaian', 'Ghanaian'), ('Greek', 'Greek'), ('Grenadian', 'Grenadian'), ('Guatemalan', 'Guatemalan'), ('Guinea-Bissauan', 'Guinea-Bissauan'), ('Guinean', 'Guinean'), ('Guyanese', 'Guyanese'), ('Haitian', 'Haitian'), ('Honduran', 'Honduran'), ('Hungarian', 'Hungarian'), ('Icelandic', 'Icelandic'), ('Indian', 'Indian'), ('Indonesian', 'Indonesian'), ('Iranian', 'Iranian'), ('Iraqi', 'Iraqi'), ('Irish', 'Irish'), ('Israeli', 'Israeli'), ('Italian', 'Italian'), ('Ivorian', 'Ivorian'), ('Jamaican', 'Jamaican'), ('Japanese', 'Japanese'), ('Jordanian', 'Jordanian'), ('Kazakh', 'Kazakh'), ('Kenyan', 'Kenyan'), ('Kiribati', 'Kiribati'), ('Kuwaiti', 'Kuwaiti'), ('Kyrgyz', 'Kyrgyz'), ('Laotian', 'Laotian'), ('Latvian', 'Latvian'), ('Lebanese', 'Lebanese'), ('Liberian', 'Liberian'), ('Libyan', 'Libyan'), ('Liechtensteiner', 'Liechtensteiner'), ('Lithuanian', 'Lithuanian'), ('Luxembourgish', 'Luxembourgish'), ('Macedonian', 'Macedonian'), ('Malagasy', 'Malagasy'), ('Malawian', 'Malawian'), ('Malaysian', 'Malaysian'), ('Maldivian', 'Maldivian'), ('Malian', 'Malian'), ('Maltese', 'Maltese'), ('Marshallese', 'Marshallese'), ('Mauritanian', 'Mauritanian'), ('Mauritian', 'Mauritian'), ('Mexican', 'Mexican'), ('Micronesian', 'Micronesian'), ('Moldovan', 'Moldovan'), ('Monacan', 'Monacan'), ('Mongolian', 'Mongolian'), ('Montenegrin', 'Montenegrin'), ('Moroccan', 'Moroccan'), ('Mozambican', 'Mozambican'), ('Namibian', 'Namibian'), ('Nauruan', 'Nauruan'), ('Nepalese', 'Nepalese'), ('New Zealander', 'New Zealander'), ('Nicaraguan', 'Nicaraguan'), ('Nigerian', 'Nigerian'), ('Nigerien', 'Nigerien'), ('North Korean', 'North Korean'), ('Norwegian', 'Norwegian'), ('Omani', 'Omani'), ('Pakistani', 'Pakistani'), ('Palauan', 'Palauan'), ('Panamanian', 'Panamanian'), ('Papua New Guinean', 'Papua New Guinean'), ('Paraguayan', 'Paraguayan'), ('Peruvian', 'Peruvian'), ('Philippine', 'Philippine'), ('Polish', 'Polish'), ('Portuguese', 'Portuguese'), ('Qatari', 'Qatari'), ('Romanian', 'Romanian'), ('Russian', 'Russian'), ('Rwandan', 'Rwandan'), ('Saint Lucian', 'Saint Lucian'), ('Salvadoran', 'Salvadoran'), ('Samoan', 'Samoan'), ('San Marinese', 'San Marinese'), ('Sao Tomean', 'Sao Tomean'), ('Saudi', 'Saudi'), ('Senegalese', 'Senegalese'), ('Serbian', 'Serbian'), ('Seychellois', 'Seychellois'), ('Sierra Leonean', 'Sierra Leonean'), ('Singaporean', 'Singaporean'), ('Slovak', 'Slovak'), ('Slovenian', 'Slovenian'), ('Solomon Islander', 'Solomon Islander'), ('Somali', 'Somali'), ('South African', 'South African'), ('South Korean', 'South Korean'), ('South Sudanese', 'South Sudanese'), ('Spanish', 'Spanish'), ('Sri Lankan', 'Sri Lankan'), ('Sudanese', 'Sudanese'), ('Surinamer', 'Surinamer'), ('Swazi', 'Swazi'), ('Swedish', 'Swedish'), ('Swiss', 'Swiss'), ('Syrian', 'Syrian'), ('Taiwanese', 'Taiwanese'), ('Tajik', 'Tajik'), ('Tanzanian', 'Tanzanian'), ('Thai', 'Thai'), ('Togolese', 'Togolese'), ('Tongan', 'Tongan'), ('Trinidadian or Tobagonian', 'Trinidadian or Tobagonian'), ('Tunisian', 'Tunisian'), ('Turkish', 'Turkish'), ('Turkmen', 'Turkmen'), ('Tuvaluan', 'Tuvaluan'), ('Ugandan', 'Ugandan'), ('Ukrainian', 'Ukrainian'), ('Uruguayan', 'Uruguayan'), ('Uzbek', 'Uzbek'), ('Vanuatuan', 'Vanuatuan'), ('Venezuelan', 'Venezuelan'), ('Vietnamese', 'Vietnamese'), ('Yemeni', 'Yemeni'), ('Zambian', 'Zambian'), ('Zimbabwean', 'Zimbabwean'), ('Not Specified', 'Not Specified')], default='Not Specified', max_length=100, null=True)),
                ('address', models.TextField(blank=True, verbose_name='Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Is Verified')),
            ],
        ),
        migrations.CreateModel(
            name='ImportedCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('select', 'Select Brand'), ('Abarth', 'Abarth'), ('Acura', 'Acura'), ('Aiways', 'Aiways'), ('Alfa Romeo', 'Alfa Romeo'), ('Alpine', 'Alpine'), ('Aptera', 'Aptera'), ('Arcfox', 'Arcfox'), ('Ariel', 'Ariel'), ('Aston Martin', 'Aston Martin'), ('Audi', 'Audi'), ('Automobili Pininfarina', 'Automobili Pininfarina'), ('BAIC', 'BAIC'), ('Baojun', 'Baojun'), ('Bentley', 'Bentley'), ('Bestune', 'Bestune'), ('Bisu', 'Bisu'), ('BMW', 'BMW'), ('Bollinger', 'Bollinger'), ('Borgward', 'Borgward'), ('Brilliance Auto', 'Brilliance Auto'), ('Buick', 'Buick'), ('BYD', 'BYD'), ('Cadillac', 'Cadillac'), ('Canoo', 'Canoo'), ('Caparo', 'Caparo'), ('Changan', 'Changan'), ('Changfeng', 'Changfeng'), ('Chery', 'Chery'), ('Chevrolet', 'Chevrolet'), ('Chrysler', 'Chrysler'), ('Citroën', 'Citroën'), ('Cupra', 'Cupra'), ('Dacia', 'Dacia'), ('Daewoo', 'Daewoo'), ('Daihatsu', 'Daihatsu'), ('Datsun', 'Datsun'), ('De Tomaso', 'De Tomaso'), ('Denza', 'Denza'), ('Detroit Electric', 'Detroit Electric'), ('DFSK', 'DFSK'), ('Dodge', 'Dodge'), ('Dongfeng', 'Dongfeng'), ('DS Automobiles', 'DS Automobiles'), ('Eagle', 'Eagle'), ('FAW', 'FAW'), ('Ferrari', 'Ferrari'), ('Fiat', 'Fiat'), ('Fisker', 'Fisker'), ('Ford', 'Ford'), ('Foton', 'Foton'), ('Geely', 'Geely'), ('Genesis', 'Genesis'), ('GMC', 'GMC'), ('Great Wall Motors', 'Great Wall Motors'), ('Haima', 'Haima'), ('Haval', 'Haval'), ('Hawtai', 'Hawtai'), ('Hennessey', 'Hennessey'), ('HiPhi', 'HiPhi'), ('Honda', 'Honda'), ('Hongqi', 'Hongqi'), ('Hummer', 'Hummer'), ('Hyundai', 'Hyundai'), ('Ineos', 'Ineos'), ('Infiniti', 'Infiniti'), ('Iran Khodro', 'Iran Khodro'), ('Isuzu', 'Isuzu'), ('JAC', 'JAC'), ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('JETTA', 'JETTA'), ('Jonway', 'Jonway'), ('Karma', 'Karma'), ('KGM (SsangYong)', 'KGM (SsangYong)'), ('Kia', 'Kia'), ('Koenigsegg', 'Koenigsegg'), ('Krajina', 'Krajina'), ('Lada', 'Lada'), ('Lamborghini', 'Lamborghini'), ('Lancia', 'Lancia'), ('Land Rover', 'Land Rover'), ('Leapmotor', 'Leapmotor'), ('Lexus', 'Lexus'), ('Li Auto', 'Li Auto'), ('Lifan', 'Lifan'), ('Lincoln', 'Lincoln'), ('Lotus', 'Lotus'), ('Lucid', 'Lucid'), ('Lynk & Co', 'Lynk & Co'), ('Mahindra', 'Mahindra'), ('Maserati', 'Maserati'), ('Maxus', 'Maxus'), ('Maybach', 'Maybach'), ('Mazda', 'Mazda'), ('McLaren', 'McLaren'), ('Mercedes-Benz', 'Mercedes-Benz'), ('MG', 'MG'), ('Mini', 'Mini'), ('Mitsubishi', 'Mitsubishi'), ('Morris Garages', 'Morris Garages'), ('NIO', 'NIO'), ('Nissan', 'Nissan'), ('Ora', 'Ora'), ('Opel', 'Opel'), ('Pagani', 'Pagani'), ('Peugeot', 'Peugeot'), ('Polestar', 'Polestar'), ('Pontiac', 'Pontiac'), ('Porsche', 'Porsche'), ('Proton', 'Proton'), ('Qoros', 'Qoros'), ('Ram', 'Ram'), ('Ravon', 'Ravon'), ('Renault', 'Renault'), ('Rimac', 'Rimac'), ('Roewe', 'Roewe'), ('Rolls-Royce', 'Rolls-Royce'), ('Rover', 'Rover'), ('Saab', 'Saab'), ('Saic MG', 'Saic MG'), ('Samsung Motors', 'Samsung Motors'), ('Seat', 'Seat'), ('Seres', 'Seres'), ('Shelby', 'Shelby'), ('Skoda', 'Škoda'), ('Smart', 'Smart'), ('Soueast', 'Soueast'), ('SsangYong', 'SsangYong'), ('Stellantis', 'Stellantis'), ('Subaru', 'Subaru'), ('Suzuki', 'Suzuki'), ('Tata', 'Tata'), ('Tatra', 'Tatra'), ('Tesla', 'Tesla'), ('Tianjin Xiali', 'Tianjin Xiali'), ('Toyota', 'Toyota'), ('Trabant', 'Trabant'), ('Triumph', 'Triumph'), ('TVR', 'TVR'), ('Vauxhall', 'Vauxhall'), ('Venucia', 'Venucia'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo'), ('Weltmeister (WM Motor)', 'Weltmeister (WM Motor)'), ('Wuling', 'Wuling'), ('Xpeng', 'Xpeng'), ('Yugo', 'Yugo'), ('Zastava', 'Zastava'), ('Zotye', 'Zotye'), ('ZX Auto', 'ZX Auto')], default='select', max_length=100, verbose_name='Brand')),
                ('model', models.CharField(max_length=100, verbose_name='Model')),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('vin', models.CharField(max_length=17, unique=True, verbose_name='VIN')),
                ('kilometer', models.PositiveIntegerField(verbose_name='Kilometers')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('fuel_type', models.CharField(choices=[('gasoline', 'Gasoline'), ('diesel', 'Diesel'), ('hybrid', 'Hybrid'), ('electric', 'Electric')], max_length=20, verbose_name='Fuel Type')),
                ('transmission', models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], max_length=20, verbose_name='Transmission')),
                ('engine_size', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Engine Size (L)')),
                ('condition_type', models.CharField(choices=[('clean_title', 'Clean Title'), ('normal_wear', 'Normal Wear'), ('exceeds_mechanical_limits', 'Exceeds Mechanical Limits'), ('biohazard', 'Biohazard / Chemical'), ('burn_engine', 'Burn - Engine'), ('burn_interior', 'Burn - Interior'), ('burn_exterior', 'Burn - Exterior'), ('damage_history', 'Damage History'), ('frame_damage', 'Frame Damage'), ('hail_damage', 'Hail Damage'), ('mechanical', 'Mechanical'), ('mileage_discrepancy', 'Mileage Discrepancy'), ('partial_repair', 'Partial Repair'), ('rejected_repair', 'Rejected Repair'), ('rollover', 'Rollover'), ('side_damage', 'Side Damage'), ('stripped', 'Stripped'), ('theft_recovery', 'Theft Recovery'), ('undercarriage_damage', 'Undercarriage Damage'), ('vandalism', 'Vandalism'), ('water_flood', 'Water / Flood'), ('all_over_damage', 'All Over Damage')], max_length=50, verbose_name='Vehicle Condition Type')),
                ('key', models.CharField(blank=True, choices=[('Has Key', 'Has Key'), ('Missing', 'Missing'), ('Other', 'Other')], max_length=50, verbose_name='Key')),
                ('auction_country', models.CharField(choices=[('USA', 'USA'), ('Canada', 'Canada'), ('Germany', 'Germany'), ('France', 'France'), ('Italy', 'Italy'), ('Netherlands', 'Netherlands'), ('Belgium', 'Belgium'), ('United Kingdom', 'United Kingdom'), ('Turkey', 'Turkey'), ('United Arab Emirates', 'United Arab Emirates'), ('Japan', 'Japan'), ('South Korea', 'South Korea'), ('China', 'China'), ('Russia', 'Russia'), ('Spain', 'Spain'), ('Poland', 'Poland'), ('Georgia', 'Georgia'), ('Ukraine', 'Ukraine')], max_length=50, verbose_name='Auction Country')),
                ('auction_house', models.CharField(max_length=100, verbose_name='Auction Company')),
                ('auction_date', models.DateField(verbose_name='Auction Date')),
                ('auction_location', models.CharField(max_length=100, verbose_name='Auction Location')),
                ('auction_price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Auction Price (zł)')),
                ('auction_fee', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Auction Fee (zł)')),
                ('purchase_date', models.DateField(verbose_name='Purchase Date')),
                ('shipping_company', models.CharField(blank=True, max_length=100, verbose_name='Shipping Company')),
                ('shipping_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Shipping Cost (zł)')),
                ('shipping_departure_date', models.DateField(blank=True, null=True, verbose_name='Shipping Departure Date')),
                ('shipping_arrival_date', models.DateField(blank=True, null=True, verbose_name='Shipping Arrival Date')),
                ('port_of_loading', models.CharField(blank=True, max_length=100, verbose_name='Port of Loading')),
                ('port_of_discharge', models.CharField(blank=True, max_length=100, verbose_name='Port of Discharge')),
                ('insurance_company', models.CharField(blank=True, max_length=100, verbose_name='Insurance Company')),
                ('insurance_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Insurance Cost (zł)')),
                ('insurance_policy_number', models.CharField(blank=True, max_length=50, verbose_name='Insurance Policy Number')),
                ('customs_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Customs Cost (zł)')),
                ('tax_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Tax Cost (zł)')),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Total Cost (zł)')),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Selling Price (zł)')),
                ('status', models.CharField(choices=[('auction', 'At Auction'), ('purchased', 'Purchased'), ('shipping', 'In Shipping'), ('customs', 'In Customs'), ('arrived', 'Arrived'), ('sold', 'Sold')], default='auction', max_length=20, verbose_name='Status')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars', to='lifeautoimport.client', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'Imported Car US',
                'verbose_name_plural': 'Imported Car US',
                'ordering': ['-auction_date'],
                'permissions': [('view_net_profit', 'Can view net profit')],
            },
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=lifeautoimport.models.car_image_path, verbose_name='Image')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Description')),
                ('image_type', models.CharField(choices=[('exterior', 'Exterior'), ('interior', 'Interior'), ('engine', 'Engine'), ('chassis', 'Chassis'), ('damage', 'Damage'), ('document', 'Document'), ('other', 'Other')], max_length=50, verbose_name='Image Type')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded At')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='lifeautoimport.importedcar')),
            ],
            options={
                'verbose_name': 'Car Image',
                'verbose_name_plural': 'Car Images',
            },
        ),
        migrations.CreateModel(
            name='CarDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to=lifeautoimport.models.car_document_path, validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png'])], verbose_name='Document')),
                ('document_type', models.CharField(choices=[('auction', 'Auction Document'), ('invoice', 'Invoice'), ('bill_of_lading', 'Bill of Lading'), ('insurance', 'Insurance Document'), ('customs', 'Customs Document'), ('registration', 'Registration Document'), ('other', 'Other')], max_length=50, verbose_name='Document Type')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Description')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Uploaded At')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='lifeautoimport.importedcar')),
            ],
            options={
                'verbose_name': 'Car Document',
                'verbose_name_plural': 'Car Documents',
            },
        ),
    ]
