from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='management_home'),
   path('add_car_vendor', views.add_car_vendor, name='add_car_vendor'),
   path('add_trip_vendor', views.add_trip_vendor, name='add_trip_vendor'),
   path('add_tour_guide', views.add_tour_guide, name='add_tour_guide'),
   path('update_user/', views.update_user, name='update_user'),
   path('delete_user/', views.delete_user, name='delete_user'),

]
