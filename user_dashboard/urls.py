from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('share_trip_data', views.share_trip_data, name='share_trip_data'),

]
