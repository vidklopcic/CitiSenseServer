from django.http import HttpResponse
from django.shortcuts import render
from CitiSense.models import Sensor, Area
import json

def format_sensor(sensor):
    return {'id': sensor.id,
            'name': sensor.name,
            'date-added': sensor.date_added.timestamp(),
            'pollutants': [str(j) for j in sensor.pollutant_set.all()],
            'lat': sensor.lat,
            'lng': sensor.lng}

def get_sensors_by_area_name(request, area_name):
    areas = Area.objects.filter(name=area_name)
    if areas:
        area = areas[0]
    else:
        return HttpResponse(json.dumps([]))
    all_sensors = [format_sensor(i) for i in area.sensor_set.all()]
    return HttpResponse(json.dumps(all_sensors))


def get_sensor_by_id(request, id):
    sensors = Sensor.objects.filter(id=id)
    if sensors:
        return HttpResponse(json.dumps(format_sensor(sensors[0])))
    else:
        return HttpResponse(json.dumps([]))

def get_measurements_from_interval(request, id, pollutant):
    try:
        start = request.GET.get('start', '')
        end = request.GET.get('stop', '')
    except:
        return HttpResponse(json.dumps([]))
    # todo

def get_areas(request):
    all_areas = [str(i) for i in Area.objects.all()]
    return HttpResponse(json.dumps(all_areas))