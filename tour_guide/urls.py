from django.urls import path, re_path
from  . import views

urlpatterns = [

    # The home page
    path('', views.index, name='tour_guide_home'),
    path('add_language', views.add_language, name='add_language'),
    path('update_language', views.update_language, name='update_language'),
    path('delete_language', views.delete_language, name='delete_language'),
    path('tour_guide_profile_info', views.tour_guide_profile_info, name='tour_guide_profile_info'),

]
