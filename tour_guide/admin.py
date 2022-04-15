from django.contrib import admin

# Register your models here.
from tour_guide.models import TourGuideProfile, Language


class TourGuideProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'city', 'mobile_number']


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['user', 'language_name', 'native', 'is_verified', 'created']


admin.site.register(TourGuideProfile, TourGuideProfileAdmin)
admin.site.register(Language, LanguageAdmin)
