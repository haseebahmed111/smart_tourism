from django.db import models
from django.contrib.auth.models import User


class Province(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Area(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    detail_link = models.URLField()
    picture = models.ImageField(upload_to='city_images', blank=True)

    def __str__(self):
        return self.name


class CustomTripOffer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city')
    to_province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='to_province')
    to_area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True, related_name='to_area')
    to_city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='to_city')
    destination_note = models.CharField(max_length=255, null=True, blank=True)
    max_budget = models.IntegerField(default=0, null=True, blank=True)
    persons = models.IntegerField(default=1, null=True, blank=True)
    min_days = models.IntegerField(default=1, null=True, blank=True)
    max_days = models.IntegerField(default=1, null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class CustomTripBid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(CustomTripOffer, on_delete=models.CASCADE)
    trip_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name='bid_from_city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='bid_to_city')
    budget = models.IntegerField(default=0)
    persons = models.IntegerField(default=0)
    days = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
