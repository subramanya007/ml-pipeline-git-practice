# model.py  (v1 - needs improvement)
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def load_clean_data(path):
    return pd.read_csv(path)

def train(df):
    X = df.drop("label", axis=1)
    y = df["label"]

    # no scaling, no tuning - just a raw model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    print(f"Accuracy: {acc:.2f}")
    return model

if __name__ == "__main__":
    df = load_clean_data("data/clean.csv")
    model = train(df)
