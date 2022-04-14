from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('share_trip_data', views.share_trip_data, name='share_trip_data'),
    path('update_trip_data/<id>', views.update_trip_data, name='update_trip_data'),
    path('delete_trip_data/<id>', views.delete_trip_data, name='delete_trip_data'),
    path('delete_trip_data_check/<id>/<check>', views.delete_trip_data_check, name='delete_trip_data'),
    path('role_elevation', views.role_elevation, name='role_elevation'),
    path('complaint', views.complaint, name='complaint'),
    #path('view_trip_data', views.view_share_trip_data, name='view_share_trip_data'),

]
