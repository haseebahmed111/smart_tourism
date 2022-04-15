from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='trip_vendor_home'),
    path('add_trip', views.add_trip, name='add_trip'),
    path('update_trip/<id>', views.update_trip, name='update_trip'),
    path('delete_trip/<id>', views.delete_trip, name='delete_trip'),
    path('delete_trip_check/<id>/<check>', views.delete_trip_check, name='delete_trip_check'),
    path('trip_vendor_profile', views.trip_vendor_profile, name='trip_vendor_profile'),
]
