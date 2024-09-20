import requests
import sqlite3
from datetime import datetime
import os

# Fetch API key from environment variables or fallback to hardcoded value
API_KEY = os.getenv('OPENWEATHER_API_KEY', '087ace64662fdd8da43c1ed5a07a8995')  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    """
    Fetches the weather data from the OpenWeatherMap API for the specified city.
    
    Args:
        city (str): The city to fetch the weather data for.
    
    Returns:
        dict: A dictionary containing city, temperature, humidity, wind speed, and time.
        None: If the API request fails.
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # for temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return weather
    else:
        print(f"Error fetching weather data for {city}.")
        return None

def store_weather_data(weather):
    """
    Stores the fetched weather data into the SQLite database.

    Args:
        weather (dict): A dictionary containing the weather data.
    """
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO weather (city, temperature, humidity, wind_speed, time)
    VALUES (?, ?, ?, ?, ?)
    ''', (weather['city'], weather['temperature'], weather['humidity'], weather['wind_speed'], weather['time']))

    conn.commit()
    conn.close()
    print(f"Weather data for {weather['city']} stored successfully.")

if __name__ == "__main__":
    city = 'Pune'
    weather = fetch_weather_data(city)
    if weather:
        store_weather_data(weather)
