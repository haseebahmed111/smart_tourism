from django.contrib import admin

# Register your models here.
from trip_vendor.models import TripVendorProfile


class TripVendorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'mobile_number']


admin.site.register(TripVendorProfile, TripVendorProfileAdmin)
