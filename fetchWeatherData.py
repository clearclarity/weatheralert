# Fetch current weather data from Weatherstack.com

import requests

API_KEY = 'your_weatherstack_api_key'
BASE_URL = 'http://api.weatherstack.com/current'

def get_weather(city_name):
    params = {
        'access_key': API_KEY,
        'query': city_name
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if 'error' not in data:
        current_weather = data['current']
        return {
            'temperature': current_weather['temperature'],
            'description': current_weather['weather_descriptions'][0],
            'humidity': current_weather['humidity'],
            'precip': current_weather['precip']
        }
    else:
        return None

# Example usage
weather_data = get_weather("YourCityName")
if weather_data:
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Weather description: {weather_data['description']}")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Precipitation: {weather_data['precip']} mm")
