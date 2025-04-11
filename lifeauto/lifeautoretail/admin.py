from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Car, CarImage, CustomerInquiry


admin.site.site_header = "LifeAuto Admin"
admin.site.site_title = "LifeAuto Admin"
admin.site.index_title = "LifeAuto Admin"


def export_cars_to_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="cars.xlsx"'
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Cars"
    
    headers = [
        'ID', 'Brand', 'Model', 'Year', 'Price', 'Kilometer', 'Color',
        'Body Type', 'Engine Size', 'Transmission', 'Fuel Type', 'Horsepower',
        'Description', 'Is Available', 'Created At', 'Updated At'
    ]
    ws.append(headers)
    
    for car in queryset:
        row = [
            car.id,
            car.brand,
            car.model,
            car.year,
            car.price,
            car.kilometer,
            car.color,
            car.get_body_type_display(),
            car.engine_size,
            car.get_transmission_display(),
            car.get_fuel_type_display(),
            car.horsepower,
            car.description,
            "Yes" if car.is_available else "No",
            car.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            car.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        ]
        ws.append(row)
    
    wb.save(response)
    return response

export_cars_to_excel.short_description = "Export to Excel"


def export_inquiries_to_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="customer_inquiries.xlsx"'
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Customer Inquiries"
    
    headers = [
        'ID', 'Car', 'Name', 'Email', 'Phone', 'Message',
        'Is Contacted', 'Created At'
    ]
    ws.append(headers)
    
    for inquiry in queryset:
        row = [
            inquiry.id,
            str(inquiry.car),
            inquiry.name,
            inquiry.email,
            inquiry.phone,
            inquiry.message,
            "Yes" if inquiry.is_contacted else "No",
            inquiry.created_at.strftime('%Y-%m-%d %H:%M:%S')
        ]
        ws.append(row)
    
    wb.save(response)
    return response

export_inquiries_to_excel.short_description = "Export to Excel"


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1
    readonly_fields = ['image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px; boder-radius: 5px;" />', 
                obj.image.url
            )
        return "-"
    image_preview.short_description = 'Preview'

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    list_display = (
        'brand', 
        'model', 
        'year', 
        'price', 
        'is_available',
        'primary_image_preview',
        'id',
    )
    list_filter = ('is_available', 'brand', 'year', 'fuel_type')
    search_fields = ('brand', 'model', 'description')
    ordering = ('-created_at',)
    readonly_fields = ['car_images_preview']
    actions = [export_cars_to_excel]
    
    def primary_image_preview(self, obj):
        primary = obj.images.filter(is_primary=True).first()
        if primary:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px; boder-radius: 5px;" />', 
                primary.image.url
            )
        return "-"
    primary_image_preview.short_description = 'Primary Image'
    
    def car_images_preview(self, obj):
        images = obj.images.all()[:5] #5 img for car 
        if images:
            return format_html(
                ' '.join(
                    '<img src="{}" style="max-height: 100px; max-width: 100px; margin-right: 10px; boder-radius: 5px;" />'.format(img.image.url) 
                    for img in images
                )
            )
        return "-"
    car_images_preview.short_description = 'All Images'

# Car images are managed in the CarImageInline above, so this is commented out because I do not prefer to show them in the admin panel separately.
# @admin.register(CarImage)
# class CarImageAdmin(admin.ModelAdmin):
#     list_display = ('car', 'image_preview', 'is_primary')
#     list_filter = ('car__brand', 'is_primary')
#     readonly_fields = ['image_preview']
    
#     def image_preview(self, obj):
#         if obj.image:
#             return format_html(
#                 '<img src="{}" style="max-height: 200px; max-width: 200px; boder-radius: 5px;" />', 
#                 obj.image.url
#             )
#         return "-"
#     image_preview.short_description = 'Preview'

@admin.register(CustomerInquiry)
class CustomerInquiryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'car_with_image', 
        'email', 
        'phone', 
        'is_contacted', 
        'created_at'
    )
    list_filter = ('is_contacted', 'car__brand')
    search_fields = ('name', 'email', 'phone', 'car__brand', 'car__model')
    ordering = ('-created_at',)
    actions = ['mark_as_contacted']
    actions = [export_cars_to_excel]
    
    def car_with_image(self, obj):
        primary = obj.car.images.filter(is_primary=True).first()
        if primary:
            return format_html(
                '{} {} {} <img src="{}" style="max-height: 50px; max-width: 50px; margin-left: 10px; boder-radius: 5px;" />', 
                obj.car.year,
                obj.car.brand,
                obj.car.model,
                primary.image.url
            )
        return f"{obj.car.year} {obj.car.brand} {obj.car.model}"
    car_with_image.short_description = 'Car'
    
    def mark_as_contacted(self, request, queryset):
        queryset.update(is_contacted=True)
    mark_as_contacted.short_description = "Mark selected inquiries as contacted"