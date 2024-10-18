from django.db import models

# Create your models here.


class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=20, unique=True)
    license_plate = models.CharField(max_length=20, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    current_location_lat = models.FloatField(null=True, blank=True)
    current_location_lng = models.FloatField(null=True, blank=True)
    STATUS = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')


class Meta:
    db_table ='vehicles'