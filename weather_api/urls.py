
from django.contrib import admin
from django.urls import path, include
from . views import WeatherView
urlpatterns = [
    path('', WeatherView.as_view()),
]
