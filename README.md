# Weather Data Aggregator and Analyzer

## Description

This project aggregates weather data from OpenWeatherMap, stores it in a SQLite database, and provides analysis and visualization of weather trends.

## Setup

1. **Create a virtual environment and activate it:**

    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your OpenWeatherMap API key:**

    ```bash
    set OPENWEATHER_API_KEY=087ace64662fdd8da43c1ed5a07a8995
    ```

4. **Create the database:**

    ```bash
    python create_database.py
    ```

## Usage

1. **Fetch weather data (manual or scheduled):**

    ```bash
    python weather_app.py
    ```

    Or:

    ```bash
    python scheduler.py
    ```

2. **Analyze weather data:**

    ```bash
    python analyze.py
    ```

3. **Visualize weather data:**

    ```bash
    python visualize.py
    ```

## Files

- `create_database.py`: Creates the SQLite database and weather data table.
- `weather_app.py`: Fetches and stores weather data.
- `analyze.py`: Analyzes weather data for specified date ranges.
- `visualize.py`: Visualizes weather trends.
- `scheduler.py`: Automatically fetches weather data at regular intervals.
- `requirements.txt`: Lists project dependencies.
- `README.md`: Project documentation.
