from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone

from apps.home.models import City


class CarVendorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=20)
    brief_info = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    policy = models.TextField(max_length=10000)
    terms_and_condition = models.TextField(max_length=10000)
    picture = models.ImageField(upload_to='car_vendor_images/', blank=True)
    is_verified = models.BooleanField(default=False)
    information_added_on = models.DateTimeField(default=timezone.now)


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(CarVendorProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    seating_capacity = models.IntegerField()
    fuel_average = models.FloatField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    driver = models.BooleanField(default=False)
    rent_with_driver = models.IntegerField(default=0)
    rent_without_driver = models.IntegerField(default=0)
    picture = models.FileField(upload_to='vendor_trip/', blank=True)
    is_verified = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
