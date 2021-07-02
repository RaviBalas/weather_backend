from django.urls import path, include

urlpatterns = [
    path('api/weather', include('weather_api.urls')),
]
