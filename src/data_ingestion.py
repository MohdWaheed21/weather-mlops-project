import pandas as pd

def load_data():
    df = pd.read_csv("data/raw/weather.csv")

    print("First 5 Rows:")
    print(df.head())

    print("\nShape of Dataset:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns)

    return df


if __name__ == "__main__":
    load_data()