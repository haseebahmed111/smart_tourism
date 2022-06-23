from django.contrib import admin
from .models import City, Area, Province


# Register your models here.

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name']


class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'province']


class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'area', 'province']


admin.site.register(Province, ProvinceAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(City, CityAdmin)
