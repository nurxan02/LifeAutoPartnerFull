from django.contrib import admin
from .models import ImportedCar, CarImage, CarDocument,Client
from django.utils.html import format_html
from decimal import Decimal
from django.db import models

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1 
    readonly_fields = ('preview_image',) 
    fields = ('preview_image','image', 'image_type')  
    def preview_image(self, obj):
        if obj.image: 
            return format_html('<img src="{}" height="500" style="border-radius: 5px;" />', obj.image.url)
        return "-"  
    preview_image.short_description = "Preview"  

class CarDocumentInline(admin.TabularInline):
    model = CarDocument
    extra = 1
    readonly_fields = ('document_link',)
    
    def document_link(self, obj):
        if obj.document:
            from django.utils.html import format_html
            return format_html('<a href="{}" target="_blank">View Document</a>', obj.document.url)
        return "-"
    document_link.short_description = "Document Link"

@admin.register(ImportedCar)
class ImportedCarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'vin', 'status', 'total_cost','selling_price','preview_image','client','key','condition_type')
    list_filter = ('status', 'brand', 'year')
    search_fields = ('vin', 'brand', 'model','client__first_name', 'client__last_name')
    inlines = [CarImageInline, CarDocumentInline]
    actions = ['calculate_total_net_profit','mark_as_arrived']
    fieldsets = (
        ('Basic Information', {
            'fields': ('client','brand', 'model', 'year', 'vin', 'kilometer', 'color', 'fuel_type', 'transmission', 'engine_size','key','condition_type')
        }),
        ('Auction Details', {
            'fields': ('auction_country','auction_house', 'auction_date', 'auction_location',
                      'auction_price', 'auction_fee', 'purchase_date')
        }),
        ('Shipping & Logistics', {
            'fields': ('shipping_company', 'shipping_cost', 
                      'shipping_departure_date', 'shipping_arrival_date',
                      'port_of_loading', 'port_of_discharge')
        }),
        ('Financials', {
            'fields': ('insurance_cost', 'customs_cost', 'tax_cost',
                      'total_cost', 'selling_price')
        }),
        ('Status & Notes', {
            'fields': ('status', 'notes')
        }),
    )

    def get_list_display(self, request):
        if request.user.has_perm('lifeautoimport.view_net_profit'):
            return self.list_display + ('net_profit_display',)
        return self.list_display

    def net_profit_display(self, obj):
        return obj.net_profit
    net_profit_display.short_description = "Net Profit (zł)"

    def calculate_total_net_profit(self, request, queryset):

        total_net_profit = sum(car.net_profit for car in queryset)
        self.message_user(request, f"Net Profit of Selected Cars: {total_net_profit} zł")
   
    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('lifeautoimport.view_net_profit'):
            if 'calculate_total_net_profit' in actions:
                del actions['calculate_total_net_profit']
        return actions
    def get_queryset(self, request):
       
        self.request = request
        return super().get_queryset(request)
    def mark_as_arrived(self, request, queryset):
        queryset.update(status='arrived')
    mark_as_arrived.short_description = "Mark selected cars as arrived"
    def preview_image(self, obj):
        primary_image = obj.images.first()  
        if primary_image and primary_image.image:
            return format_html('<img src="{}" height="100" style="border-radius: 5px;" />', primary_image.image.url)
        return "-"
    preview_image.short_description = "Preview"

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'created_at','is_verified')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('is_verified',)
    list_editable=('is_verified',)
    ordering = ('-created_at',)

