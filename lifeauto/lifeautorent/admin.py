from django.contrib import admin
from django.utils.html import format_html  
from django import forms
from .models import EBike, Bike, Scooter, Car, Client, ClientDocument, ClientPayments,ClientPenalties
from django.http import HttpResponse
from openpyxl import Workbook
import openpyxl

def export_to_excel(modeladmin, request, queryset):
    model_name = modeladmin.model.__name__
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{model_name.lower()}s.xlsx"'
    
    wb = Workbook()
    ws = wb.active
    ws.title = model_name + "s"

    headers = []
    fields = []
    
    if model_name == 'EBike':
        headers = ['ID', 'Name', 'Brand', 'Battery Capacity (kWh)', 'Max Speed (km/h)', 
                  'Price Per Week', 'Is Active','Client', 'Image Path']
        fields = ['id', 'name', 'brand', 'battery_capacity', 'max_speed', 
                 'price_per_week', 'is_active','client', 'image']
    
    elif model_name == 'Bike':
        headers = ['ID', 'Name', 'Brand', 'Gear Count', 'Price Per Week', 
                  'Is Active','Client', 'Image Path']
        fields = ['id', 'name', 'brand', 'gear_count', 'price_per_week', 
                 'is_active','client', 'image']
    
    elif model_name == 'Scooter':
        headers = ['ID', 'Name', 'Brand', 'Max Speed (km/h)', 'Price Per Week', 
                  'Is Active', 'Client', 'Image Path']
        fields = ['id', 'name', 'brand', 'max_speed', 'price_per_week', 
                 'is_active','client', 'image']
    
    elif model_name == 'Car':
        headers = ['ID', 'Name', 'Brand', 'Category', 'Seating Capacity', 
                  'Price Per Week', 'Is Active', 'Client', 'Image Path']
        fields = ['id', 'name', 'brand', 'get_category_display', 'seating_capacity', 
                 'price_per_week', 'is_active','client', 'image']
    
    ws.append(headers)
    

    for obj in queryset:
        row = []
        for field in fields:
            if hasattr(obj, field):
                value = getattr(obj, field)

                if field == 'get_category_display':
                    value = obj.get_category_display()
                elif field == 'image':
                    value = str(obj.image) if obj.image else ""
                elif field == 'client':
                    value = str(value)
                elif isinstance(value, bool):
                    value = "Yes" if value else "No"
                row.append(value)
        ws.append(row)
    
    wb.save(response)
    return response

export_to_excel.short_description = "Export to Excel"

@admin.register(EBike)
class EBikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand','sku', 'battery_capacity', 'max_speed', 'price_per_week', 'is_active', 'image_preview')
    search_fields = ('name', 'brand','sku')
    list_filter = ('is_active', )
    list_editable = ('is_active', )
    readonly_fields = ('image_preview', 'sku',)
    actions = [export_to_excel]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand','sku', 'gear_count', 'price_per_week', 'is_active', 'image_preview')
    search_fields = ('name', 'brand','sku')
    list_filter = ('is_active', )
    list_editable = ('is_active', )
    readonly_fields = ('image_preview', 'sku',)
    actions = [export_to_excel]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"


@admin.register(Scooter)
class ScooterAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand','sku', 'max_speed', 'price_per_week', 'is_active', 'image_preview')
    search_fields = ('name', 'brand','sku')
    list_filter = ('status','is_active', )
    list_editable = ('is_active', )
    readonly_fields = ('image_preview', 'sku',)
    actions = [export_to_excel]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"
  

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand','sku', 'category', 'seating_capacity', 'price_per_week', 'is_active', 'image_preview')
    search_fields = ('name', 'brand', 'category','sku')
    list_filter = ('is_active', 'category')
    list_editable = ('is_active', )
    readonly_fields = ('image_preview', 'sku',)
    actions = [export_to_excel]


    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"



def export_clients_to_excel(modeladmin, request, queryset):
   
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Clients"

   
    headers = [
        "First Name", "Last Name", "Email", "Phone Number", "Nationality",
        "Address", "Is Contacted", "Is Verified", "Total Payments", 
        "Total Penalties", "Rented Vehicles", "Status",  "Created At", "Updated At"
    ]
    sheet.append(headers)

  
    for client in queryset:
        sheet.append([
            client.first_name,
            client.last_name,
            client.email,
            client.phone_number,
            client.nationality,
            client.address,
            "Yes" if client.is_contacted else "No",
            "Yes" if client.is_verified else "No",
            client.total_payments(), 
            client.total_penalties(),  
            client.rented_vehicles(),  
            client.status,
            client.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            client.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        ])

  
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = 'attachment; filename="clients.xlsx"'
    workbook.save(response)
    return response

export_clients_to_excel.short_description = "Export selected clients to Excel"


class ClientDocumentInline(admin.TabularInline):
    model = ClientDocument
    extra = 1  
    fields = ('document', 'description', 'uploaded_at','expire') 
    readonly_fields = ('uploaded_at',)

class ClientPayments(admin.TabularInline):
    model=ClientPayments
    extra=1
    fields=('description','refundable','payment_interests','created_at')
    readonly_fields = ('created_at',)

class ClientPenalties(admin.TabularInline):
    model=ClientPenalties
    extra=1
    fields=('description','penalty_fee','status','created_at')
    readonly_fields = ('created_at',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number',  'total_payments','total_penalties','rented_vehicles', 'status')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('is_contacted', 'is_verified', 'nationality')
    ordering = ('-created_at',)
    inlines = [ClientDocumentInline, ClientPayments,ClientPenalties]
    actions = [export_clients_to_excel]