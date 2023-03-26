import requests

from skin_choice import choose_time_skin

url = 'https://api.weatherapi.com/v1/current.json'

with open('.env', 'r') as f:
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
