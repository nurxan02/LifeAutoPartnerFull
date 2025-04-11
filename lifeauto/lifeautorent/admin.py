from django.contrib import admin
from django.utils.html import format_html  
from .models import EBike, Bike, Scooter, Car
from django.http import HttpResponse
from openpyxl import Workbook

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
                  'Price Per Week', 'Is Active', 'Image Path']
        fields = ['id', 'name', 'brand', 'battery_capacity', 'max_speed', 
                 'price_per_week', 'is_active', 'image']
    
    elif model_name == 'Bike':
        headers = ['ID', 'Name', 'Brand', 'Gear Count', 'Price Per Week', 
                  'Is Active', 'Image Path']
        fields = ['id', 'name', 'brand', 'gear_count', 'price_per_week', 
                 'is_active', 'image']
    
    elif model_name == 'Scooter':
        headers = ['ID', 'Name', 'Brand', 'Max Speed (km/h)', 'Price Per Week', 
                  'Is Active', 'Image Path']
        fields = ['id', 'name', 'brand', 'max_speed', 'price_per_week', 
                 'is_active', 'image']
    
    elif model_name == 'Car':
        headers = ['ID', 'Name', 'Brand', 'Category', 'Seating Capacity', 
                  'Price Per Week', 'Is Active', 'Image Path']
        fields = ['id', 'name', 'brand', 'get_category_display', 'seating_capacity', 
                 'price_per_week', 'is_active', 'image']
    
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

                elif isinstance(value, bool):
                    value = "Yes" if value else "No"
                row.append(value)
        ws.append(row)
    
    wb.save(response)
    return response

export_to_excel.short_description = "Export to Excel"

@admin.register(EBike)
class EBikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'battery_capacity', 'max_speed', 'price_per_week', 'is_active', 'image_preview')
    search_fields = ('name', 'brand')
    list_filter = ('is_active', )
    list_editable = ('is_active', )
    readonly_fields = ('image_preview', )
    actions = [export_to_excel]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'gear_count', 'price_per_week', 'is_active', 'image_preview')
    search_fields = ('name', 'brand')
    list_filter = ('is_active', )
    list_editable = ('is_active', )
    readonly_fields = ('image_preview', )
    actions = [export_to_excel]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"


@admin.register(Scooter)
class ScooterAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'max_speed', 'price_per_week', 'is_active', 'image_preview')
    search_fields = ('name', 'brand')
    list_filter = ('is_active', )
    list_editable = ('is_active', )
    readonly_fields = ('image_preview', )
    actions = [export_to_excel]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'seating_capacity', 'price_per_week', 'is_active', 'image_preview')
    search_fields = ('name', 'brand', 'category')
    list_filter = ('is_active', 'category')
    list_editable = ('is_active', )
    readonly_fields = ('image_preview', )
    actions = [export_to_excel]


    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"