from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class ShareTrip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    from_place = models.CharField(max_length=255)
    to_place = models.CharField(max_length=255)
    vehicle = models.CharField(max_length=255)
    date = models.DateField()
    persons = models.IntegerField()
    budget_spent = models.IntegerField()
    budget_spent_food = models.IntegerField()
    budget_spent_hotel = models.IntegerField()
    heading = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image = models.FileField(upload_to='trips/', null=True)
