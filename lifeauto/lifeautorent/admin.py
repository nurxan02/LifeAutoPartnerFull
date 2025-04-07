from django.contrib import admin
from django.utils.html import format_html  
from .models import EBike, Bike, Scooter, Car

@admin.register(EBike)
class EBikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'battery_capacity', 'max_speed', 'price_per_week', 'is_active', 'image_preview')
    search_fields = ('name', 'brand')
    list_filter = ('is_active', )
    list_editable = ('is_active', )
    readonly_fields = ('image_preview', )

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

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius:5px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"