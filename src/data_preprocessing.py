import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):
    print("Starting preprocessing...")

    # Step 1: Remove row ID column
    if "row ID" in df.columns:
        df = df.drop("row ID", axis=1)

    # Step 2: Remove missing values
    df = df.dropna()

    print("After removing null values:", df.shape)

    # Step 3: Convert target column
    le = LabelEncoder()

    df["RainTomorrow"] = le.fit_transform(df["RainTomorrow"])
    df["RainToday"] = le.fit_transform(df["RainToday"])

    # Step 4: Convert remaining text columns
    categorical_columns = df.select_dtypes(include=["object"]).columns

    for col in categorical_columns:
        df[col] = le.fit_transform(df[col])

    # Step 5: Separate features and target
    X = df.drop("RainTomorrow", axis=1)
    y = df["RainTomorrow"]

    # Step 6: Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Training data shape:", X_train.shape)
    print("Testing data shape:", X_test.shape)

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    df = pd.read_csv("data/raw/weather.csv")
    preprocess_data(df)