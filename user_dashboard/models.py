from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from apps.home.models import City


class ShareTrip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="DepartureCity")
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="ArrivalCity")
    vehicle = models.CharField(max_length=255)
    date = models.DateField()
    trip_duration = models.IntegerField(default=0)
    persons = models.IntegerField()
    total_budget_spent = models.IntegerField(default=0)
    budget_spent_food = models.IntegerField(default=0)
    budget_spent_accommodation = models.IntegerField(default=0)
    budget_spent_travelling = models.IntegerField(default=0)
    description = models.TextField(max_length=1024)
    cover = models.FileField(upload_to='trips/')
    shared_on = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} | {self.from_city} - {self.to_city}'


class SharedTripImage(models.Model):
    trip = models.ForeignKey(ShareTrip, on_delete=models.CASCADE)
    image = models.FileField(upload_to='trips/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class SharedTripVideoLink(models.Model):
    trip = models.ForeignKey(ShareTrip, on_delete=models.CASCADE)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)


class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)

    complaint_description = models.TextField(max_length=1024)
    is_resolved = models.BooleanField(default=False)


class RoleElevationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    role = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    info = models.CharField(max_length=10000)
    role_given = models.BooleanField(default=False)
    requested_on = models.DateTimeField(default=timezone.now)
