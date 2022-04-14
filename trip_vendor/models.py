from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class TripVendorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    brief_info = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    policy = models.TextField(max_length=10000)
    terms_and_condition = models.TextField(max_length=10000)
    picture = models.ImageField(upload_to='trip_vendor_images/', blank=True)
    is_verified = models.BooleanField(default=False)
    information_added_on = models.DateTimeField(default=timezone.now)
