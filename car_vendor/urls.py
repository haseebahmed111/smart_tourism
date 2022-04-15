from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='car_vendor_home'),
    path('add_car', views.add_car, name='add_car'),
    path('delete_car/<id>', views.delete_car, name='delete_car'),
    path('delete_car_check/<id>/<check>', views.delete_car_check, name='delete_car_check'),
    path('update_car/<id>', views.update_car, name='update_car'),
    path('car_vendor_profile', views.car_vendor_profile, name='car_vendor_profile'),
]
