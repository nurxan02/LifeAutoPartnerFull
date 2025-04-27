from django.contrib import admin
from .models import Blog, Contact, BlogImage, ImportedVehicleAdvertisament, VehicleAdvertisementImage, CustomerInquiryImport,AllCustomersCRM
from django.utils.html import format_html

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("message_category","name", "email", "tel", "message", "checkmark", "is_connected")
    search_fields = ("name", "email", "tel")
    list_editable = ("checkmark","is_connected")

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 0

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"

    fields = ('image', 'image_preview') 
    readonly_fields = ('image_preview', )  


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'created_at', 'updated_at', 'active', ) 
    search_fields = ('title', 'description')
    list_filter = ('active', )  
    list_editable = ('active', )
    inlines = [BlogImageInline]  

class VehicleAdvertisementImageInline(admin.TabularInline):
    model = VehicleAdvertisementImage
    extra = 1
    fields = ('image', 'preview_image',  'uploaded_at')
    readonly_fields = ('preview_image', 'uploaded_at')

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="200" style="border-radius: 5px;" />', obj.image.url)
        return "-"
    preview_image.short_description = "Preview"

@admin.register(ImportedVehicleAdvertisament)
class VehicleAdvertisamentAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'title', 'price', 'created_at', 'updated_at')
    search_fields = ('brand', 'model', 'title')
    list_filter = ('created_at', 'updated_at')
    inlines = [VehicleAdvertisementImageInline]

@admin.register(CustomerInquiryImport)
class CustomerInquiryImportAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)
    ordering = ('-created_at',)    
@admin.register(AllCustomersCRM)
class AllCustomersCRMAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'platform','is_contacted')
    search_fields = ('name', 'surname', 'phone', 'platform')
    list_filter = ('created_at','platform')
    ordering = ('-created_at',)
    list_editable =('is_contacted',)