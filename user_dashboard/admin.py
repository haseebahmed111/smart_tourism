from django.contrib import admin
from .models import ShareTrip, Complaint, RoleElevationRequest


# Register your models here.

class ShareTripAdmin(admin.ModelAdmin):
    list_display = ['user', 'from_city', 'to_city', 'shared_on', 'is_approved']


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'is_resolved']


class RoleElevationRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'contact_number', 'role_given']


admin.site.register(ShareTrip, ShareTripAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(RoleElevationRequest, RoleElevationRequestAdmin)
