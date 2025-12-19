#Weather API logic
import datetime
import os
import requests
import json
from config import Config


API_KEY = Config.API_KEY


class WeatherAPI:

    def fetch_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        weather_info = {}
        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            weather_info = {
            "city": data["name"],
            "temperature": round(temperature),
            "temp_min": round(temp_min),
            "temp_max": round(temp_max),
            "description": data["weather"][0]["description"],
            "main": data["weather"][0]["main"],   
            "date": str(datetime.datetime.now().strftime("%A, %B %d"))
        }
        return weather_info
    
    

