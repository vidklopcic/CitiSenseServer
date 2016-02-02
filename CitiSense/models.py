from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Area(models.Model):
    name = models.CharField(max_length=20, unique=True)
    lat_top = models.FloatField()
    lng_top = models.FloatField()
    lat_bot = models.FloatField()
    lng_bot = models.FloatField()

    def __str__(self):
        return self.name

class Sensor(models.Model):
    name = models.CharField(max_length=20)
    area = models.ForeignKey(Area)
    date_added = models.DateTimeField()
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name

class Pollutant(models.Model):
    sensor = models.ManyToManyField(Sensor)
    short_name = models.CharField(max_length=5, unique=True)
    long_name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.short_name

class Measurement(models.Model):
    date_time = models.DateTimeField()
    pollutant = models.ForeignKey(Pollutant)
    sensor = models.ForeignKey(Sensor)
    value = models.FloatField()
    unit = models.CharField(max_length=10)
    accuracy = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    def __str__(self):
        return self.pollutant.short_name + ' ' + str(self.value) + ' ' + self.unit