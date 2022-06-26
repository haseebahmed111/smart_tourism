from django.contrib import admin
from .models import ShareTrip, Complaint, RoleElevationRequest, SharedTripImage, SharedTripVideoLink


# Register your models here.

class ShareTripAdmin(admin.ModelAdmin):
    list_display = ['user', 'from_city', 'to_city', 'shared_on', 'is_approved']


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'is_resolved']


class RoleElevationRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'contact_number', 'role_given']


class SharedTripImageAdmin(admin.ModelAdmin):
    list_display = ['trip', 'created']


class SharedTripVideoLinkAdmin(admin.ModelAdmin):
    list_display = ['trip', 'created']


admin.site.register(ShareTrip, ShareTripAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(RoleElevationRequest, RoleElevationRequestAdmin)
admin.site.register(SharedTripImage, SharedTripImageAdmin)
admin.site.register(SharedTripVideoLink, SharedTripVideoLinkAdmin)
