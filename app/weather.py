import redis
import json
import datetime
import requests
from config import Config

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

API_KEY = Config.API_KEY


class WeatherAPI:

    def fetch_weather(self, city):
        city = city.lower().strip()

        # cache key (hourly)
        current_hour = datetime.datetime.now().strftime("%Y-%m-%d-%H")
        cache_key = f"weather:{city}:{current_hour}"

        
        cached_data = redis_client.get(cache_key)
        if cached_data:
            print(f"Using cached weather for {city}")
            return json.loads(cached_data)
        else:
            print(f"Fetching new weather for {city}")
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        if response.status_code != 200:
            return None

        data = response.json()

        weather_info = {
            "city": data["name"],
            "temperature": round(data["main"]["temp"]),
            "temp_min": round(data["main"]["temp_min"]),
            "temp_max": round(data["main"]["temp_max"]),
            "description": data["weather"][0]["description"],
            "main": data["weather"][0]["main"],
            "date": datetime.datetime.now().strftime("%A, %B %d, %H:00")
        }

        
        redis_client.setex(
            cache_key,
            3600,
            json.dumps(weather_info)
        )

        return weather_info

    
    

