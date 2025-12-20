#Build and configure the app
from flask import Flask, render_template, request
import requests
import weather as Weather

weatherApp = Weather.WeatherAPI()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("weather.html")

@app.route("/weather", methods = ["POST", "GET"])
def getWeather():

    cityName = ""
    weather = {}
    weatherIcon = ""  

    if request.method == "POST":
        try:
            cityName = request.form["city"]
        except KeyError:
            return render_template("weather.html", error="Please enter a city name.")
        
        if not cityName.strip():
            return render_template("weather.html", error="City name cannot be empty.")

        try:
            weather = weatherApp.fetch_weather(cityName)
            weatherName = weather["main"]
            cityName = weather["city"]
        except (KeyError, TypeError):
                return render_template("weather.html", error="City not found or invalid data.")
        except requests.RequestException:
            return render_template("weather.html", error="Could not fetch weather data.")
        
        if weatherName == "Clear":
            weatherIcon = "sun"
        elif weatherName == "Clouds":
            weatherIcon = "cloud"
        elif weatherName == "Rain":
            weatherIcon = "cloud-rain"
        elif weatherName == "Snow":
            weatherIcon = "snowflake"
        elif weatherName == "Drizzle":
            weatherIcon = "cloud-rain"
        elif weatherName == "Thunderstorm":
            weatherIcon = "cloud-bolt"
        elif weatherName in ["Mist", "Smoke", "Haze", "Dust", "Fog", "Sand", "Ash", "Squall", "Tornado"]:
            weatherIcon = "smog"
        elif weatherName == "Wind":
            weatherIcon = "wind"

    return render_template("result.html", cityName = cityName, weather = weather, weatherIcon = weatherIcon)



if __name__ == '__main__':
    app.run(debug=True)