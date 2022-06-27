from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trip/<id>', views.view_trip, name='view_trip'),
    path('car/<id>', views.view_car, name='view_car'),
    path('shared_trip/<id>', views.view_shared_trip, name='view_shared_trip'),
    path('delete_shared_trip_image/<trip_id>/<id>', views.delete_shared_trip_image, name='delete_shared_trip_image'),
    path('login/', views.home_login, name='home_login'),
    path('signup/', views.signup, name='home_signup'),
    path('guide/tour/<id>', views.view_tour_guide_profile, name='view_tour_guide_profile'),
    path('vendor/trip/<id>', views.view_trip_vendor_profile, name='view_trip_vendor_profile'),
    path('vendor/car/<id>', views.view_car_vendor_profile, name='view_car_vendor_profile'),
    path('private_trip', views.create_private_trip, name='create_private_trip'),
    path('private_trip/<id>', views.view_private_trip, name='view_private_trip'),
    path('vendor/trip/detect/<id>/', views.detect_trip_vendor, name='detect_trip_vendor'),

    # path('vendor/car/<id>', views.car_vendor_profile, name='car_vendor_profile'),
    # path('car_vendor', views.car_vendor, name='car_vendor'),
    # path('tour_guide', views.tour_guide, name='tour_guide'),
    # path('vendor', views.vendor, name='vendor'),
    # path('update_trip', views.update_trip, name='update_trip'),
    # path('search', views.search, name='search'),
    # path('search/q=<text>', views.search, name='search'),
    # path('share_data', views.share_data, name='share_data'),

]
