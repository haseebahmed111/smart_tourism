from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from apps.home.models import City


class TourGuideProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    languages = models.CharField(max_length=255)
    brief_info = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    policy = models.TextField(max_length=10000)
    terms_and_condition = models.TextField(max_length=10000)
    picture = models.ImageField(upload_to='tour_guide_images/', blank=True)
    is_verified = models.BooleanField(default=False)
    information_added_on = models.DateTimeField(default=timezone.now)


class Language(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language_name = models.CharField(max_length=255)
    native = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
