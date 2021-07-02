import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Weather
from .serializers import WeatherSerializer


class WeatherView(APIView):
    @staticmethod
    def get(request):
        try:
            if 'city' in request.GET:
                try:
                    instance = Weather.objects.get(city__iexact=request.GET['city'])
                    serializer = WeatherSerializer(instance)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Weather.DoesNotExist as e:
                    params = {'q': request.GET['city'], "appid": settings.WEATHER_KEY}
                    response_data = requests.get(url=r"https://api.openweathermap.org/data/2.5/weather",
                                                 params=params).json()
                    if int(response_data['cod']) == 200:
                        data = {'city': response_data['name'],
                                'weather_description': response_data['weather'][0]['description'],
                                'temperature': response_data['main']['temp'],
                                'pressure': response_data['main']['pressure'],
                                'humidity': response_data['main']['humidity'],
                                'wind_speed': response_data['wind']['speed']
                                }
                        serializer = WeatherSerializer(data=data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data, status=status.HTTP_200_OK)
                        else:
                            return Response(data="city not exist+", status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(data="city not exist-", status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(data="please enter city", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data="please contact support", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
