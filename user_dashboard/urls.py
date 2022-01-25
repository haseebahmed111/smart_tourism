from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('share_trip_data', views.share_trip_data, name='share_trip_data'),
    path('update_trip_data', views.update_trip_data, name='update_trip_data'),
    path('delete_trip_data', views.delete_trip_data, name='delete_trip_data'),
    #path('view_trip_data', views.view_share_trip_data, name='view_share_trip_data'),

]
