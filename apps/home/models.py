from django.db import models
from django.contrib.auth.models import User


# Create your models here.


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
