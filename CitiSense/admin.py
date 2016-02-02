from django.contrib import admin
from .models import Sensor, Pollutant, Measurement, Area

# Register your models here.
admin.site.register(Sensor)
admin.site.register(Pollutant)
admin.site.register(Measurement)
admin.site.register(Area)