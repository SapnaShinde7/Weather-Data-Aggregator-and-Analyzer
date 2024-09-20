import schedule
import time
from weather_app import fetch_weather_data, store_weather_data

def job():
    city = 'Pune'  
    weather = fetch_weather_data(city)
    if weather:
        store_weather_data(weather)

# Schedule the job to run every hour
schedule.every().hours.do(job)

print("Scheduler started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
