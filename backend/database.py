import sqlite3


def create_table():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prediction_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location INTEGER,
            temperature REAL,
            humidity REAL,
            pressure REAL,
            rain_today INTEGER,
            prediction TEXT
        )
    """)

    conn.commit()
    conn.close()

    print("Database and table created successfully!")


if __name__ == "__main__":
    create_table()
