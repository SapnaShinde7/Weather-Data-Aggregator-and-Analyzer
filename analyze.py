import sqlite3
import pandas as pd

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

def calculate_statistics(city, start_date, end_date):
    """
    Calculates and prints the average temperature and humidity for the given city and date range.
    
    Args:
        city (str): The city for which to calculate statistics.
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.
    """
    df = fetch_data_for_analysis(city, start_date, end_date)
    
    if df.empty:
        print(f"No data found for {city} in the given date range.")
        return
    
    avg_temp = df['temperature'].mean()
    avg_humidity = df['humidity'].mean()
    print(f"Average Temperature for {city} from {start_date} to {end_date}: {avg_temp:.2f}°C")
    print(f"Average Humidity for {city} from {start_date} to {end_date}: {avg_humidity:.2f}%")

if __name__ == "__main__":
    city = input("Enter the city for analysis: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    calculate_statistics(city, start_date, end_date)
