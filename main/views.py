from django.shortcuts import render
from django.contrib import messages
import requests
# https://api.openweathermap.org/data/2.5/weather?q=kathmandu&appid=6d2e400206202418fd767656b3a8a1d7
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# apikey='6d2e400206202418fd767656b3a8a1d7'

# Create your views here.


def index(request):
    temperature = ''
    humidity = ''
    wind_speed = ''
    city = ''

    if 'city' in request.POST:
        city = request.POST['city']
        api_key = '6d2e400206202418fd767656b3a8a1d7'
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        # Make HTTP request to OpenWeatherMap API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
        else:
           messages.success(request,'Incorrect city name ')
        

    return render(request, 'weather.html', {'temperature': temperature, 'humidity': humidity, 'wind_speed': wind_speed, 'city': city})
