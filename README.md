🌦 Weather Forecast & Alert Application
📌 Project Overview

The Weather Forecast & Alert Application is a Python-based full-stack project that provides real-time weather updates, 7-day forecasts, and automated weather alerts for any city in the world.

It integrates multiple weather APIs, processes live data, generates insights, and displays results through a FastAPI backend and a Streamlit dashboard.

This project demonstrates skills in:
API Integration
Backend Development (FastAPI)
Data Processing
Visualization
Automation & Alert System
Real-world system design

🎯 Problem Statement
Weather conditions impact:
Travel plans ✈️
Agriculture 🌾
Logistics 🚚
Outdoor events 🎪
Safety management ⚠️

People need a system that:
Fetches real-time weather data
Provides forecast for upcoming days
Generates alerts for extreme weather conditions
Displays data in a user-friendly format

💡 Solution
This project solves the problem by:

Fetching live weather data using APIs
Processing and analyzing weather conditions
Generating alerts for:
Heatwaves 🔥
High humidity 💧
Strong winds 🌪
Displaying results via API and dashboard

🛠 Tech Stack
Python 3.x
FastAPI
Streamlit
Requests
Pandas
Matplotlib
Open-Meteo API
OpenWeatherMap API (optional multi-provider system)
Uvicorn

🏗 Project Architecture
User Input (City)
        ↓
Geocoding API (Get Latitude/Longitude)
        ↓
Weather APIs (Open-Meteo / OpenWeather)
        ↓
Data Processing & Analysis
        ↓
Alert Engine (Rule-Based System)
        ↓
FastAPI Backend Response
        ↓
Streamlit Dashboard Visualization

📁 Folder Structure
Weather_Forecast_Alert_App/
│
├── api/
│   └── app.py                 # FastAPI backend
│
├── outputs/                  # Generated charts
├── reports/                  # Excel / CSV reports
├── images/                   # Screenshots
│
├── app.py                    # Streamlit dashboard
├── forecast_visualization.py # Data visualization script
├── requirements.txt
├── .env                      # API keys (NOT uploaded to GitHub)
├── .gitignore
└── README.md

⚙️ Installation Guide
1️⃣ Clone Repository
git clone <your-repo-link>
cd Weather_Forecast_Alert_App
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Environment (Windows Fix Included)

If error occurs: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
Then activate: venv\Scripts\Activate

4️⃣ Install Dependencies
pip install -r requirements.txt

▶️ How to Run Project
🔹 Run FastAPI Backend
uvicorn api.app:app --reload

Open:
http://127.0.0.1:8000/weather?city=Delhi
🔹 Run Streamlit Dashboard
streamlit run app.py

🌦 Features
🌍 Real-time weather data
📊 7-day forecast visualization
⚠ Weather alert system
📍 City-based search
📈 Temperature & rainfall graphs
🔁 Multi-API integration (Open-Meteo + OpenWeather)
📊 Interactive dashboard
🧠 Rule-based weather intelligence
⚠️ Weather Alerts System

The system generates alerts for:
🔥 Temperature > 40°C → Heatwave Alert
💧 Humidity > 80% → High Humidity Alert
🌪 Wind speed > threshold → Wind Alert

🌐 API Usage Example
GET /weather?city=Nagpur
Response:
{
  "city": "Nagpur",
  "temperature": 35.2,
  "humidity": 60,
  "wind_speed": 12.5,
  "alerts": ["Heatwave Alert"],
  "forecast": [...]
}

📸 Screenshots
Dashboard UI
Forecast Graph
API Response
Alerts Output

🚀 Learning Outcomes
This project helped me learn:
REST API development
Weather data integration
Data analysis & visualization
Backend system design
Error handling in APIs
Real-world project structuring

🔮 Future Improvements
AI-based weather prediction
Push notifications (SMS/Email/Telegram)
Map-based weather visualization
Mobile app version
AQI integration
Multi-region forecasting

🧑‍💻 Author
Anjali Meshram
Computer Science & Engineering Student
Python Developer | Aspiring Data Engineer

⭐ If you like this project
Give a ⭐ on the repository and connect on LinkedIn!