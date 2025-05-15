from django.contrib import admin
from .models import RegistrationPartner,PartnerCarsList,PartnerCarsLicenses
from django.http import HttpResponse
from django.db.models import Model
from openpyxl import Workbook

def export_to_excel(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="registration_partners.xlsx"'
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Registration Partners"
    
    # qaqamn title-i 
    headers = [
        'ID', 'First Name', 'Last Name', 'Email', 
        'Country Code', 'Phone Number', 'Nationality',
        'Languages', 'Date of Birth', 'Street', 'Floor Number',
        'Postcode', 'City', 'Has Bank Account', 'Bank Account Number',
        'Is Student', 'Is Over 26', 'Has Company', 'Apps', 'Created At'
    ]
    ws.append(headers)
    
    # qaqamn datasi
    for obj in queryset:
        languages = ", ".join(obj.languages) if obj.languages else ""
        apps = ", ".join(obj.apps) if obj.apps else ""
        
        row = [
            obj.id,
            obj.first_name,
            obj.last_name,
            obj.email,
            obj.country_code,
            obj.phone_number,
            obj.get_nationality_display(),
            languages,
            obj.date_of_birth.strftime('%d-%m-%Y'),
            obj.street,
            obj.floor_number or "",
            obj.postcode,
            obj.city,
            "Yes" if obj.has_bank_account else "No",
            obj.bank_account_number or "",
            "Yes" if obj.is_student else "No",
            "Yes" if obj.is_over_26 else "No",
            "Yes" if obj.has_company else "No",
            apps,
            obj.created_at.strftime('%Y-%m-%d %H:%M:%S')
        ]
        ws.append(row)
    
    wb.save(response)
    return response

export_to_excel.short_description = "Export to Excel"

@admin.register(RegistrationPartner)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "nationality", "date_of_birth","created_at")
    search_fields = ("first_name", "last_name", "email", "nationality")
    list_filter = ("nationality", "is_student", "has_company", "is_over_26")
    actions = [export_to_excel]


class PartnerCarsLicensesInline(admin.TabularInline):
    model = PartnerCarsLicenses
    extra = 1  
    fields = ('partner_car', 'city', 'status')
    readonly_fields = ('partner_car', )

@admin.register(PartnerCarsList)
class PartnerCarsListAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "purpose", "sign_number", "vin", "owner", "client", "status")
    search_fields = ("brand", "model", "vin", "owner", "client")
    list_filter = ("brand", "model", "purpose")
    inlines = [PartnerCarsLicensesInline]
