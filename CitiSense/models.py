from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    date_added = models.DateTimeField()

class Pollutant(models.Model):
    sensor = models.ForeignKey(Sensor)
    short_name = models.CharField(unique=True)
    long_name = models.CharField(unique=True)
    description = models.CharField()
    unit = models.CharField()

class Measurement(models.Model):
    date_time = models.DateTimeField()
    pollutant = models.ForeignKey(Pollutant)
    value = models.FloatField()
    accuracy = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])