import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('weather_data.db')

# Create a cursor
cursor = conn.cursor()

# Create a table to store weather data if it doesn't exist already
cursor.execute('''
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    humidity REAL,
    wind_speed REAL,
    time TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
