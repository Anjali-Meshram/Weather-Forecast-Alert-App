import requests
import matplotlib.pyplot as plt
import os

city = input("Enter city name: ")

# Geocoding API
geo_url = (
    f"https://geocoding-api.open-meteo.com/v1/search?"
    f"name={city}&count=1"
)

geo_response = requests.get(geo_url)

geo_data = geo_response.json()

if "results" not in geo_data:
    print("City not found")
    exit()

location = geo_data["results"][0]

latitude = location["latitude"]
longitude = location["longitude"]

# Weather Forecast API
weather_url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
    f"&forecast_days=7"
    f"&timezone=auto"
)

weather_response = requests.get(weather_url)

weather_data = weather_response.json()

daily = weather_data["daily"]

dates = daily["time"]
max_temp = daily["temperature_2m_max"]
min_temp = daily["temperature_2m_min"]
rainfall = daily["precipitation_sum"]

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# Temperature Trend Graph
plt.figure(figsize=(10,5))

plt.plot(dates, max_temp, marker='o', label="Max Temp")
plt.plot(dates, min_temp, marker='o', label="Min Temp")

plt.title(f"7-Day Temperature Forecast - {city}")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()

temp_chart_path = f"outputs/{city}_temperature_forecast.png"

plt.savefig(temp_chart_path)

print(f"Temperature chart saved: {temp_chart_path}")

plt.close()

# Rainfall Graph
plt.figure(figsize=(10,5))

plt.bar(dates, rainfall)

plt.title(f"7-Day Rainfall Forecast - {city}")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")

rain_chart_path = f"outputs/{city}_rainfall_forecast.png"

plt.savefig(rain_chart_path)

print(f"Rainfall chart saved: {rain_chart_path}")

plt.close()