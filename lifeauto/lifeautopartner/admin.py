from django.contrib import admin
from .models import RegistrationPartner

@admin.register(RegistrationPartner)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "nationality", "date_of_birth","created_at")
    search_fields = ("first_name", "last_name", "email", "nationality")
    list_filter = ("nationality", "is_student", "has_company", "is_over_26")
