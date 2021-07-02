from django.db import models


# Create your models here.
class Weather(models.Model):
    city = models.CharField(primary_key=True, max_length=20)
    weather_description = models.CharField(max_length=200, null=True)
    temperature = models.FloatField(default=0, null=True)
    pressure = models.FloatField(default=0, null=True)
    humidity = models.FloatField(null=True, default=0)
    wind_speed = models.FloatField(null=True, default=0)
