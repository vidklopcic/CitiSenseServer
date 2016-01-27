from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    date_added = models.DateTimeField()
    lat = models.FloatField()
    lng = models.FloatField()

class Pollutant(models.Model):
    sensor = models.ForeignKey(Sensor)
    short_name = models.CharField(max_length=5, unique=True)
    long_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200)
    unit = models.CharField(max_length=10)

class Measurement(models.Model):
    date_time = models.DateTimeField()
    pollutant = models.ForeignKey(Pollutant)
    value = models.FloatField()
    accuracy = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])