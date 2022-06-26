from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trip/<id>', views.view_trip, name='view_trip'),
    path('shared_trip/<id>', views.view_shared_trip, name='view_shared_trip'),
    path('delete_shared_trip_image/<trip_id>/<id>', views.delete_shared_trip_image, name='delete_shared_trip_image'),
    path('login', views.home_login, name='home_login'),
    path('car_vendor', views.car_vendor, name='car_vendor'),
    path('tour_guide', views.tour_guide, name='tour_guide'),
    path('vendor', views.vendor, name='vendor'),
    path('private_trip', views.private_trip, name='private_trip'),
    path('update_trip', views.update_trip, name='update_trip'),
    path('search', views.search, name='search'),
    path('search/q=<text>', views.search, name='search'),
    path('share_data', views.share_data, name='share_data'),
    path('signup', views.signup, name='home_signup'),

]
