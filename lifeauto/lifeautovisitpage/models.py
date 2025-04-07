from django.utils.html import format_html
from django.db import models
import os
import uuid
from django.utils.text import slugify

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
    checkmark = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.email})"
    
