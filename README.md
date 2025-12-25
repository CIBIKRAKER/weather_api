# Weather API Flask App with Redis Caching

A simple Flask web app that fetches and displays weather data for a given city using the OpenWeatherMap API.  
Caching is implemented with **Redis** to reduce repeated API calls within the same hour.

---

## Features

- Search weather by city name
- Displays:
  - Current temperature
  - Min/Max temperature
  - Weather description
  - Weather icon (Font Awesome)
- Caching using Redis (1 hour per city)
- Error handling for invalid or missing city names
- Hourly timestamp for cached weather data

---

## Requirements

- Python 3.11+
- Redis running locally (`localhost:6379`)
- Flask
- Requests
- redis-py

---

## Installation & Setup (All-in-One)


# 1. Clone the repo
    git clone <your-repo-url>
    cd weather-api-flask

# 2. Create and activate a virtual environment
    python -m venv venv
# Windows
    venv\Scripts\activate
# Linux / Mac
    source venv/bin/activate

# 3. Install dependencies
    pip install -r requirements.txt

# 4. Create config.py with your OpenWeatherMap API key
    class Config:
    API_KEY = "your_openweathermap_api_key_here"

# 5. Start Redis server (Windows example)
# Navigate to folder where redis-server.exe is located
    cd C:\Redis
    .\redis-server.exe

# 6. Run the Flask app
    cd <your-project-folder>
    python main.py
