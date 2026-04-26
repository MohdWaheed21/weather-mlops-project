import joblib
import pandas as pd


def predict_rain():
    print("Loading trained model...")

    model = joblib.load("model/rain_prediction.pkl")

    print("Model loaded successfully!")

    # Example user input
    sample_data = {
        "Location": 2,
        "MinTemp": 13.4,
        "MaxTemp": 22.9,
        "Rainfall": 0.6,
        "Evaporation": 5.0,
        "Sunshine": 8.0,
        "WindGustDir": 3,
        "WindGustSpeed": 44,
        "WindDir9am": 5,
        "WindDir3pm": 7,
        "WindSpeed9am": 20,
        "WindSpeed3pm": 24,
        "Humidity9am": 71,
        "Humidity3pm": 22,
        "Pressure9am": 1007.7,
        "Pressure3pm": 1007.1,
        "Cloud9am": 8,
        "Cloud3pm": 7,
        "Temp9am": 16.9,
        "Temp3pm": 21.8,
        "RainToday": 0
    }

    input_df = pd.DataFrame([sample_data])

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        print("Prediction: Rain Tomorrow ☔")
    else:
        print("Prediction: No Rain Tomorrow ☀")


if __name__ == "__main__":
    predict_rain()