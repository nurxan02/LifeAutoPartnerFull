from django.utils.html import format_html
from django.db import models
import os
import uuid
from django.utils.text import slugify
from PIL import Image

def blog_main_image_upload_to(instance, filename):
    blog_name = slugify(instance.title)
    unique_id = str(uuid.uuid4())[:4]
    extension = os.path.splitext(filename)[1]
    new_filename = f"{blog_name}-{unique_id}{extension}"
    return os.path.join('blog_images/', new_filename)

class Blog(models.Model):
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    content = models.TextField()  
    image = models.ImageField(upload_to=blog_main_image_upload_to)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  
    active = models.BooleanField(default=True)  

    def image_preview(self):
        if self.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius:5px;" />', self.image.url)
        return "No Image"
    image_preview.short_description = "Image Preview"

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Promotions"
        verbose_name_plural = "Promotions"
        ordering = ['-created_at']


def blog_image_upload_to(instance, filename):
    blog_name = slugify(instance.blog.title)
    unique_id = uuid.uuid4()
    extension = os.path.splitext(filename)[1]
    new_filename = f"{blog_name}-{unique_id}{extension}"
    return os.path.join('blog_images/', new_filename)

class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=blog_image_upload_to)

    def __str__(self):
        return f"Image for {self.blog.title}"
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    message = models.TextField()
    checkmark = models.BooleanField(default=False, verbose_name="Acceped our regulations")
    MESSAGE_CATEGORY_CHOICES = [
        ('select', 'Select Category ...'),
        ('import', 'Import a vehicle'),
        ('rent', 'Rent a vehicle'),
        ('sell', 'Sell a vehicle'),
        ('service', 'Service'),
        ('insurance', 'Insurance'),
        ('finance', 'Finance'),
        ('buy', 'Buy a car'),
        ('general', 'General Inquiry'),
        ('support', 'Support Request'),
        ('feedback', 'Feedback'),
    ]
    message_category = models.CharField(max_length=20, choices=MESSAGE_CATEGORY_CHOICES,null=True, blank=True, default='other')
    is_connected = models.BooleanField(default=False, null=True, blank=True)    
    def __str__(self):
        return f"{self.name} ({self.email})"
    class Meta:
        verbose_name = "Customer Messages - Contact"
        verbose_name_plural = "Customer Messages - Contact"


    
class ImportedVehicleAdvertisament(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Brand")
    model = models.CharField(max_length=100, verbose_name="Model")
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Price (zł)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    def __str__(self):
        return f"{self.brand} {self.model} - {self.price} zł"
    

def advertisement_image_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{instance.advertisement.brand}_{instance.advertisement.model}_{uuid.uuid4().hex[:8]}.{ext}"
    return os.path.join('import_advertisement_images/', new_filename)


class VehicleAdvertisementImage(models.Model):
    advertisement = models.ForeignKey(
        ImportedVehicleAdvertisament, 
        on_delete=models.CASCADE, 
        related_name='images', 
        verbose_name="Advertisement"
    )
    image = models.ImageField(upload_to=advertisement_image_path, verbose_name="Image")
   
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Uploaded At")

    def save(self, *args, **kwargs):
        from io import BytesIO
        from django.core.files.base import ContentFile

        # Open the image
        img = Image.open(self.image)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Compress the image
        img_io = BytesIO()
        img.save(img_io, format='JPEG', quality=70)
        img_io.seek(0)

        # Replace the original image with the compressed one
        self.image.save(self.image.name, ContentFile(img_io.read()), save=False)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the image file from the file system
        if self.image and os.path.exists(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Vehicle Advertisement Image"
        verbose_name_plural = "Vehicle Advertisement Images"

class CustomerInquiryImport(models.Model):
    car = models.ForeignKey(ImportedVehicleAdvertisament, on_delete=models.CASCADE, related_name='inquiries')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    is_contacted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.car}"
    
    class Meta:
        verbose_name = "Customer Inquiry - Import"
        verbose_name_plural = "Customer Inquiry - Import"

class AllCustomersCRM(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20,null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    CHOICE_PLATFORMS=(
        ('friend', 'Friend referance'),
        ('website', 'Website'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('google', 'Google'),
        ('x', 'X'),
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('linkedin', 'LinkedIn'),
        ('tiktok', 'TikTok'),
        ('youtube', 'YouTube'),
        ('snapchat', 'Snapchat'),
        ('telegram', 'Telegram'),
        ('pinterest', 'Pinterest'),
        ('reddit', 'Reddit'),
        ('twitch', 'Twitch'),
        ('forum', 'Forum'),
        ('blog', 'Blog'),
        ('podcast', 'Podcast'),
    )
    platform = models.CharField(max_length=100, null=True, blank=True, choices=CHOICE_PLATFORMS)
    is_contacted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    def __str__(self):
        return f"{self.name} {self.surname} - {self.platform}"
    class Meta:
        verbose_name = "All Customers CRM"
        verbose_name_plural = "All Customers CRM"