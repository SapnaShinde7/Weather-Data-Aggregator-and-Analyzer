import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_data_for_analysis(city, start_date, end_date):
    """
    Fetches weather data for the specified city within the provided date range.
    
    Args:
        city (str): The city to fetch the weather data for.
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
        pd.DataFrame: A dataframe containing the weather data for the given city and date range.
    """
    conn = sqlite3.connect('weather_data.db')
    query = '''
    SELECT * FROM weather
    WHERE LOWER(city) = LOWER(?) AND time BETWEEN ? AND ?
    '''
    df = pd.read_sql(query, conn, params=[city, f"{start_date} 00:00:00", f"{end_date} 23:59:59"])
    conn.close()
    print(df)  # Debug print
    return df

def plot_weather_data(city, start_date, end_date):
    """
    Plots temperature and humidity trends for the specified city within the given date range.
    
    Args:
        city (str): The city to visualize data for.
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.
    """
    df = fetch_data_for_analysis(city, start_date, end_date)
    
    if df.empty:
        print(f"No data found for {city} in the given date range.")
        return
    
    # Temperature Trend
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='time', y='temperature', data=df, marker='o', label='Temperature')
    plt.title(f"Temperature Trend in {city} from {start_date} to {end_date}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Humidity Trend
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='time', y='humidity', data=df, marker='o', label='Humidity', color='green')
    plt.title(f"Humidity Trend in {city} from {start_date} to {end_date}")
    plt.xlabel("Time")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    city = input("Enter the city to visualize data for: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    plot_weather_data(city, start_date, end_date)
