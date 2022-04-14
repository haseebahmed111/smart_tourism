from django.contrib import admin


# Register your models here.
from tour_guide.models import TourGuideProfile


class TourGuideProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name','city', 'mobile_number']


admin.site.register(TourGuideProfile, TourGuideProfileAdmin)
