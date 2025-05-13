from django.contrib import admin
from .models import Report
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class ReportInline(admin.TabularInline):
    model = Report
    fields = ('date', 'message')
    readonly_fields = ('date', 'message')
    can_delete = False
    extra = 0
    def save_model(self, request, obj, form, change):
        obj.employee = request.user
        super().save_model(request, obj, form, change)

class CustomUserAdmin(UserAdmin):
    inlines = [ReportInline] 
    list_display = UserAdmin.list_display  

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)

        if not request.user.is_superuser:
            return [fs for fs in fieldsets if fs[0] not in ("Permissions", "Important dates")]

        return fieldsets

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            queryset = queryset.filter(id=request.user.id)  
        return queryset

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'message')
    readonly_fields = ('date',)

    exclude = ('employee',) 

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset  
        return queryset.filter(employee=request.user)  

    def has_add_permission(self, request, obj=None):
        return request.user.is_staff 

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return obj is not None and obj.employee == request.user  
    def save_model(self, request, obj, form, change):
        if not obj.pk: 
            obj.employee = request.user
        super().save_model(request, obj, form, change)
admin.site.register(Report, ReportAdmin)