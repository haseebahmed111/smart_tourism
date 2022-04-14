from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='city_images', blank=True)

    def __str__(self):
        return self.name
