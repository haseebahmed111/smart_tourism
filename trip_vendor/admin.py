from django.contrib import admin

# Register your models here.
from trip_vendor.models import TripVendorProfile, Trip


class TripVendorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'mobile_number']


class TripAdmin(admin.ModelAdmin):
    list_display = ['user', 'trip_from', 'trip_to', 'is_verified', 'created']


admin.site.register(TripVendorProfile, TripVendorProfileAdmin)
admin.site.register(Trip, TripAdmin)
