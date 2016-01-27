from django.conf.urls import url
# from django.contrib import admin

urlpatterns = [
    url(r'^sensors$', 'CitiSense.views.get_sensors'),
]