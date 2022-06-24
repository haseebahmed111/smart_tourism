from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

from apps.home.models import City


class TripVendorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    brief_info = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    policy = models.TextField(max_length=10000)
    terms_and_condition = models.TextField(max_length=10000)
    picture = models.FileField(upload_to='trip_vendor_images/', blank=True)
    is_verified = models.BooleanField(default=False)
    information_added_on = models.DateTimeField(default=timezone.now)


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    trip_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name="TripDepartureCity")
    trip_to = models.ForeignKey(City, on_delete=models.CASCADE, related_name="TripArrivalCity")
    accommodation = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    guide = models.BooleanField(default=False)
    other_expenses = models.BooleanField(default=False)
    departure_info = models.CharField(max_length=255)
    services_included = models.TextField(max_length=10000)
    services_not_included = models.TextField(max_length=10000)
    trip_price_per_person = models.IntegerField(default=0)
    trip_duration = models.IntegerField(default=0)
    picture = models.FileField(upload_to='vendor_trip/', blank=True)
    is_verified = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
