import sqlite3

def check_data():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    query = "SELECT * FROM weather"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    check_data()
