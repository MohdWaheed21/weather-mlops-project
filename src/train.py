import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from data_preprocessing import preprocess_data


def train_model():
    print("Loading dataset...")

    df = pd.read_csv("data/raw/weather.csv")

    print("Preprocessing data...")
    X_train, X_test, y_train, y_test = preprocess_data(df)

    print("Starting MLflow tracking...")

    with mlflow.start_run():

        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        print("Training model...")
        model.fit(X_train, y_train)

        print("Making predictions...")
        predictions = model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        print(f"Model Accuracy: {accuracy * 100:.2f}%")

        # Log parameters
        mlflow.log_param("model_type", "RandomForestClassifier")
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("random_state", 42)

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)

        # Log model
        mlflow.sklearn.log_model(
            model,
            "rain_prediction_model"
        )

        print("Saving model locally...")
        joblib.dump(
            model,
            "model/rain_prediction.pkl"
        )

        print("Model saved successfully!")
        print("MLflow tracking completed!")


if __name__ == "__main__":
    train_model()
