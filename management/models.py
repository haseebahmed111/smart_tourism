from django.db import models


# Create your models here.

class WebsiteSettings(models.Model):
    number_of_objects = models.IntegerField(default=10)
