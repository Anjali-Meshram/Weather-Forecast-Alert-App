import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# User Input
city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(BASE_URL, params=params)

    data = response.json()

    if response.status_code != 200:
        print("Error fetching weather data")
        print(data)
        exit()

    # Extract weather data
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n===== WEATHER REPORT =====")

    print(f"City: {city}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {weather}")
    print(f"Wind Speed: {wind_speed} m/s")

except Exception as e:
    print("Error:", e)