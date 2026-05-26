import requests
from datetime import datetime

class WeatherService:

    def __init__(self, api_key):

        self.api_key = api_key

        self.base_url = (
            "https://api.openweathermap.org/data/2.5/weather"
        )

    def get_weather_by_city(self, city_name):

        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric"
        }

        response = requests.get(
            self.base_url,
            params=params
        )

        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "timestamp": datetime.now()
        }