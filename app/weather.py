#Weather API logic
import os
import requests
import json
from config import Config


API_KEY = Config.API_KEY


class WeatherAPI:

    def __init__(self):
        self.weather = {}

    def fetch_weather(self, city):
        try:
            if(os.path.exists("weather.json")):
                with open("weather.json", "r") as file:
                    self.weather = json.load(file)
            else:
                self.weather = {}
        except ValueError:
            self.weather = {}
            

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_info = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
        self.weather = weather_info

        with open("weather.json", "w") as file:
            json.dump(self.weather, indent=4, fp=file)

        print(self.weather)
        return self.weather
    
    

