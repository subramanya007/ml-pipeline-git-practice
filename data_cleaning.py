# data_cleaning.py  (v1 - needs improvement)
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean(df):
    # drop nulls - very basic
    df = df.dropna()

    # rename columns - hardcoded, fragile
    df.columns = ['age', 'income', 'score', 'label']

    # remove duplicates
    df = df.drop_duplicates()

    return df

def save(df, path):
    df.to_csv(path, index=False)

if __name__ == "__main__":
    df = load_data("data/raw.csv")
    df = clean(df)
    save(df, "data/clean.csv")
    print("Done")
