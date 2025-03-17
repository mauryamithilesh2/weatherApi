from django.shortcuts import render
import requests
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# Create your views here.
def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "90826dbc219a90a52aee1eacde91800e"
    parameters = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=parameters)
    if response.status_code == 200:
        return response.json()
    else:  # response.status_code==404
        return None




def home(req):
    city = req.POST.get('city')
    icon_url = 'https://openweathermap.org/img/wn/10d@2x.png'


    weather = None
    weather_description = None
    country = None
    wind_speed = None
    pressure = None
    humidity = None
    temperature = None

    if city:
        weatherdata = get_weather(city)

        if weatherdata is not None:
            icon_id = weatherdata['weather'][0]['icon']
            icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"

            # Initialize variable with API data
            weather = weatherdata['weather'][0]['main']
            weather_description = weatherdata['weather'][0]['description']
            city = weatherdata['name']
            country = weatherdata['sys']['country']
            wind_speed = weatherdata['wind']['speed']
            pressure = weatherdata['main']['pressure']
            humidity = weatherdata['main']['humidity']
            temperature = weatherdata['main']['temp']

    return render(req, 'weather_app/index.html', {
        'icon_url': icon_url,
        'weather': weather,
        'weather_description': weather_description,
        'city': city,
        'country': country,
        'wind_speed': wind_speed,
        'pressure': pressure,
        'humidity': humidity,
        'temperature': temperature,
    })


    