from django.conf.urls import url
from django.contrib import admin
import CitiSense.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^areas$', CitiSense.views.get_areas),
    url(r'^areas/(?P<area_name>\w+)/sensors$', CitiSense.views.get_sensors_by_area_name),
    url(r'^sensors/(?P<id>\d+)$', CitiSense.views.get_sensor_by_id),
    url(r'^sensors/(?P<id>\d+)/(?P<pollutant>\w+)/measurements$', CitiSense.views)
]