from django.contrib import admin
from .models import CarVendorProfile, Car


# Register your models here.
class CarVendorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'mobile_number']


class CarAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'make', 'model', 'year', 'created']


admin.site.register(CarVendorProfile, CarVendorProfileAdmin)
admin.site.register(Car, CarAdmin)
