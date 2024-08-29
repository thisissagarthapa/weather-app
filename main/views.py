import requests
from django.shortcuts import render
from django.contrib import messages
import matplotlib.pyplot as plt
import io
import base64

def create_chart(temperature, humidity, wind_speed):
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(['Temperature', 'Humidity', 'Wind Speed'], [temperature, humidity, wind_speed])
    ax.set_ylabel('Value')
    ax.set_title('Weather Data')

    # Save to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    
    return chart_base64

def index(request):
    temperature = ''
    humidity = ''
    wind_speed = ''
    city = ''
    chart = ''  # Initialize chart variable

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = "kathmandu"
        
    api_key = '6d2e400206202418fd767656b3a8a1d7'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        chart = create_chart(temperature, humidity, wind_speed)  # Generate chart
    except:
        temperature = "0"
        humidity = "0"
        wind_speed = "0"
        messages.error(request, 'Incorrect city name or API error')

    return render(request, 'weather.html', {
        'temperature': temperature,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'city': city,
        'chart': chart
    })
