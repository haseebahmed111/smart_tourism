from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # add this
from . import settings

urlpatterns = [
                  path('admin/', admin.site.urls),  # Django admin route
                  path("account/", include("apps.authentication.urls")),
                  path("tour_guide/", include("tour_guide.urls")),
                  path("car_vendor/", include("car_vendor.urls")),
                  path("trip_vendor/", include("trip_vendor.urls")),
                  path("management/", include("management.urls")),
                  path("", include("apps.home.urls")),
                  path("user/", include("user_dashboard.urls")),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
