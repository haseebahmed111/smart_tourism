from django.contrib import admin
from .models import CarVendorProfile


# Register your models here.
class CarVendorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'mobile_number']


admin.site.register(CarVendorProfile, CarVendorProfileAdmin)
