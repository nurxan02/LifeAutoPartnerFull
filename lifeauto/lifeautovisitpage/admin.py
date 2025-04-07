from django.contrib import admin
from .models import Blog, Contact, BlogImage
from django.utils.html import format_html

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "tel", "message", "checkmark")
    search_fields = ("name", "email", "tel")

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