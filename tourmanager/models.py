from django.db import models
from django.contrib.auth.models import User


class Regions(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=30, blank=False)
    map_location = models.CharField(max_length=255, blank=True)
    region_featured_image = models.ImageField(upload_to='regions')


class Destinations(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    region = models.ForeignKey(Regions, on_delete=models.PROTECT)
    destination_name = models.CharField(max_length=30, blank=False)
    map_location = models.CharField(max_length=255, blank=True)
    destination_image = models.ImageField(upload_to='destinatiions')


class Tours(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    tour_name = models.CharField(max_length=30, blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    min_number_of_people = models.CharField(max_length=4, blank=False)
    max_number_of_people = models.CharField(max_length=4, blank=False)
    tour_price = models.FloatField(max_length=20, blank=False)


class TourData(models.Model):
    tourid = models.ForeignKey(Tours, on_delete=models.PROTECT)
    region = models.ForeignKey(Regions, on_delete=models.PROTECT)
    destination = models.ForeignKey(Destinations, on_delete=models.PROTECT)
    number_of_days = models.CharField(max_length=3, blank=True)

