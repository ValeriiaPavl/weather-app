import requests
from datetime import time

url = 'https://api.weatherapi.com/v1/current.json'

with open('w_api_key.txt', 'r') as f:
    api_key = f.read()


def is_city_real(city):
    params = {'key': api_key, 'q': city, 'aqi': 'no'}
    resp_code = requests.get(url, params=params).status_code
    if 400 <= resp_code < 500:
        return False
    return True


def fetch_weather(city, city_id):
    params = {'key': api_key, 'q': city, 'aqi': 'no'}
    weather_data = requests.get(url, params=params).json()
    temperature = int(weather_data["current"]["temp_c"])
    weather_state = weather_data["current"]["condition"]["text"]
    current_time = weather_data["location"]["localtime"]

    return {'city': city, 'city_id': city_id,
            'degrees': temperature, 'state': weather_state,
            'skin': choose_time_skin(current_time)}


def choose_time_skin(local_datetime: str):
    local_time = local_datetime.split(' ')[1]
    time_hours, time_minutes = [int(n) for n in local_time.split(':')]
    local_time_for_comparing = time(time_hours, time_minutes)

    start_day = time(hour=10, minute=0)
    end_day = time(hour=18, minute=0)
    start_night = time(hour=22, minute=0)
    end_night = time(hour=6, minute=0)

    if start_day < local_time_for_comparing < end_day:
        return "card day"
    if local_time_for_comparing > start_night or local_time_for_comparing < end_night:
        return "card night"
    else:
        return "card evening-morning"
