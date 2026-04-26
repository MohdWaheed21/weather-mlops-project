
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
import sqlite3

from backend.schema import WeatherInput


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


app = FastAPI()

# Auto-create DB table when app starts
create_table()

# CORS Fix
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained ML model
model = joblib.load("model/rain_prediction.pkl")


@app.get("/")
def home():
    return {
        "message": "Weather Prediction API is Running"
    }


@app.post("/predict")
def predict(data: WeatherInput):
    try:
        sample_data = {
            "Location": data.Location,

            "MinTemp": data.Temp9am - 5,
            "MaxTemp": data.Temp9am + 5,

            "Rainfall": 0,
            "Evaporation": 5,
            "Sunshine": 8,

            "WindGustDir": 3,
            "WindGustSpeed": 30,

            "WindDir9am": 5,
            "WindDir3pm": 7,

            "WindSpeed9am": 15,
            "WindSpeed3pm": 20,

            "Humidity9am": data.Humidity9am,
            "Humidity3pm": max(data.Humidity9am - 20, 0),

            "Pressure9am": data.Pressure9am,
            "Pressure3pm": data.Pressure9am - 2,

            "Cloud9am": 5,
            "Cloud3pm": 5,

            "Temp9am": data.Temp9am,
            "Temp3pm": data.Temp9am + 4,

            "RainToday": data.RainToday
        }

        input_df = pd.DataFrame([sample_data])

        print("Columns Sent to Model:")
        print(input_df.columns)

        print("Input Data:")
        print(input_df)

        prediction = model.predict(input_df)

        if prediction[0] == 1:
            result = "Rain Tomorrow ☔"
        else:
            result = "No Rain Tomorrow ☀"

        # Save prediction to database
        conn = sqlite3.connect("weather.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO prediction_history
            (
                location,
                temperature,
                humidity,
                pressure,
                rain_today,
                prediction
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data.Location,
            data.Temp9am,
            data.Humidity9am,
            data.Pressure9am,
            data.RainToday,
            result
        ))

        conn.commit()
        conn.close()

        return {
            "prediction": result
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/history")
def get_history():
    try:
        conn = sqlite3.connect("weather.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM prediction_history
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()
        conn.close()

        history = []

        for row in rows:
            history.append({
                "id": row[0],
                "location": row[1],
                "temperature": row[2],
                "humidity": row[3],
                "pressure": row[4],
                "rain_today": row[5],
                "prediction": row[6]
            })

        return {
            "history": history
        }

    except Exception as e:
        return {
            "error": str(e)
        }

