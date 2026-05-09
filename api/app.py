from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")  # or OPENWEATHER_API_KEY if you prefer

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Stable Weather API Running Successfully"}


@app.get("/weather")
def get_weather(city: str):

    # ---------------- GEO API ----------------
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url).json()

    if "results" not in geo_data or len(geo_data["results"]) == 0:
        return {
            "status": "error",
            "message": "City not found"
        }

    location = geo_data["results"][0]
    lat = location["latitude"]
    lon = location["longitude"]
    country = location.get("country", "Unknown")

    # ---------------- OPEN-METEO ----------------
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        f"&forecast_days=7&timezone=auto"
    )

    weather_response = requests.get(weather_url)

    if weather_response.status_code != 200:
        return {
            "status": "error",
            "message": "Open-Meteo API failed"
        }

    weather_data = weather_response.json()

    current = weather_data.get("current", {})
    daily = weather_data.get("daily", {})

    meteo_temp = current.get("temperature_2m", 0)
    meteo_humidity = current.get("relative_humidity_2m", 0)
    meteo_wind = current.get("wind_speed_10m", 0)

    # ---------------- OPENWEATHER ----------------
    openweather_data = {}

    try:
        ow_url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={city}&appid={API_KEY}&units=metric"
        )

        ow_response = requests.get(ow_url)
        openweather_data = ow_response.json()

        if ow_response.status_code != 200:
            raise Exception("OpenWeather API error")

        ow_main = openweather_data.get("main", {})
        ow_wind_data = openweather_data.get("wind", {})

        ow_temp = ow_main.get("temp", 0)
        ow_humidity = ow_main.get("humidity", 0)
        ow_wind = ow_wind_data.get("speed", 0) * 3.6

    except:
        # fallback values if API fails
        ow_temp = 0
        ow_humidity = 0
        ow_wind = 0

    # ---------------- AVERAGE ----------------
    temperature = round((meteo_temp + ow_temp) / 2, 2)
    humidity = round((meteo_humidity + ow_humidity) / 2, 2)
    wind_speed = round((meteo_wind + ow_wind) / 2, 2)

    # ---------------- ALERTS ----------------
    alerts = []

    if temperature >= 40:
        alerts.append("Heatwave Alert")

    if humidity >= 80:
        alerts.append("High Humidity Alert")

    if wind_speed >= 40:
        alerts.append("High Wind Alert")

    # ---------------- FORECAST ----------------
    forecast_data = []

    times = daily.get("time", [])

    for i in range(len(times)):
        forecast_data.append({
            "date": times[i],
            "max_temp": daily.get("temperature_2m_max", [])[i],
            "min_temp": daily.get("temperature_2m_min", [])[i],
            "rainfall": daily.get("precipitation_sum", [])[i]
        })

    # ---------------- FINAL RESPONSE ----------------
    return {
        "status": "success",
        "city": city,
        "country": country,

        "average_weather": {
            "temperature": temperature,
            "humidity": humidity,
            "wind_speed": wind_speed
        },

        "provider_data": {
            "open_meteo": {
                "temperature": meteo_temp,
                "humidity": meteo_humidity,
                "wind_speed": meteo_wind
            },
            "openweather": {
                "temperature": ow_temp,
                "humidity": ow_humidity,
                "wind_speed": ow_wind
            }
        },

        "alerts": alerts,
        "forecast": forecast_data
    }