#Build and configure the app
from flask import Flask, render_template, request
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

    if request.method == "POST":
        cityName = request.form["city"]
        weather = weatherApp.fetch_weather(cityName)
    
    return render_template("result.html", cityName = cityName, weather = weather)



if __name__ == '__main__':
    app.run(debug=True)