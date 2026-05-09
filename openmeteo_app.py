import requests
import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt
# City Coordinates
# Nagpur Example
latitude = 21.1458
longitude = 79.0882

# Open-Meteo API URL
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

try:
    response = requests.get(url)

    data = response.json()

    current = data["current"]

    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind_speed = current["wind_speed_10m"]

    print("\n===== WEATHER REPORT =====")

    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} km/h")

    # Alerts
    alerts = []

    if temperature > 40:
        alerts.append("⚠️ Heatwave Alert")

    if humidity > 80:
        alerts.append("⚠️ High Humidity Alert")

    if wind_speed > 40:
        alerts.append("⚠️ High Wind Alert")

    print("\n===== ALERTS =====")

    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("No Alerts")

except Exception as e:
    print("Error:", e)

# Create report data
report = {
    "Temperature": [temperature],
    "Humidity": [humidity],
    "Wind Speed": [wind_speed],
    "Date": [datetime.now()]
}

# Convert to DataFrame
df = pd.DataFrame(report)

# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)

# File path
report_path = "reports/weather_report.csv"

# Save CSV
df.to_csv(report_path, index=False)

print(f"\nExcel Report Saved Successfully: {report_path}")

''' we had csv file for excel file we can use following code
# Create reports folder
os.makedirs("reports", exist_ok=True)

# Excel file path
report_path = "reports/weather_report.xlsx"

# Save as Excel///
with pd.ExcelWriter(report_path, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Weather Report")

    workbook = writer.book
    worksheet = writer.sheets["Weather Report"]

    # Bold headers
    from openpyxl.styles import Font

    bold_font = Font(bold=True)

    for cell in worksheet[1]:
        cell.font = bold_font

    # Adjust column width
    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass

        adjusted_width = max_length + 5
        worksheet.column_dimensions[column_letter].width = adjusted_width

print(f"\nExcel Report Saved Successfully: {report_path}") '''

    # Create labels and values
labels = ["Temperature", "Humidity", "Wind Speed"]
values = [temperature, humidity, wind_speed]

# Create graph
plt.figure(figsize=(7,5))

plt.bar(labels, values)

# Graph title
plt.title("Weather Report")

# Y-axis label
plt.ylabel("Values")

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# Save chart
chart_path = "outputs/weather_chart.png"

plt.savefig(chart_path)

print(f"\nChart Saved Successfully: {chart_path}")