import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.title("🌦 Weather Forecast & Alert System")

# Input
city = st.text_input("Enter City Name", "Nagpur")

if st.button("Get Weather"):

    # Geocoding API
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url).json()

    if "results" not in geo_data:
        st.error("City not found")
    else:

        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        country = location["country"]

        # Weather API
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}"
            f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
            f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
            f"&forecast_days=7&timezone=auto"
        )

        data = requests.get(url).json()

        current = data["current"]
        daily = data["daily"]

        # ================= CURRENT WEATHER =================
        st.subheader(f"📍 {city}, {country}")

        col1, col2, col3 = st.columns(3)

        col1.metric("🌡 Temperature", f"{current['temperature_2m']} °C")
        col2.metric("💧 Humidity", f"{current['relative_humidity_2m']} %")
        col3.metric("🌬 Wind Speed", f"{current['wind_speed_10m']} km/h")

        # ================= ALERTS =================
        st.subheader("⚠ Alerts")

        alerts = []

        if current["temperature_2m"] > 40:
            alerts.append("🔥 Heatwave Alert")

        if current["relative_humidity_2m"] > 80:
            alerts.append("💧 High Humidity Alert")

        if current["wind_speed_10m"] > 40:
            alerts.append("🌪 High Wind Alert")

        if alerts:
            for a in alerts:
                st.error(a)
        else:
            st.success("No major alerts")

        # ================= FORECAST TABLE =================
        st.subheader("📅 7-Day Forecast")

        df = pd.DataFrame({
            "Date": daily["time"],
            "Max Temp": daily["temperature_2m_max"],
            "Min Temp": daily["temperature_2m_min"],
            "Rainfall": daily["precipitation_sum"]
        })

        st.dataframe(df)

        # ================= TEMPERATURE GRAPH =================
        st.subheader("📈 Temperature Trend")

        fig, ax = plt.subplots()
        ax.plot(df["Date"], df["Max Temp"], label="Max Temp")
        ax.plot(df["Date"], df["Min Temp"], label="Min Temp")
        ax.set_ylabel("Temperature (°C)")
        ax.legend()
        plt.xticks(rotation=45)

        st.pyplot(fig)

        # ================= RAINFALL GRAPH =================
        st.subheader("🌧 Rainfall Trend")

        fig2, ax2 = plt.subplots()
        ax2.bar(df["Date"], df["Rainfall"])
        ax2.set_ylabel("Rainfall (mm)")
        plt.xticks(rotation=45)

        st.pyplot(fig2)