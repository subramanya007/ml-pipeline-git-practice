# main.py - pipeline entry point
from src.data_cleaning import load_data, clean, save
from src.model import load_clean_data, train

def run_pipeline():
    print("=== Step 1: Data Cleaning ===")
    df = load_data("data/raw.csv")
    df = clean(df)
    save(df, "data/clean.csv")

    print("\n=== Step 2: Model Training ===")
    df_clean = load_clean_data("data/clean.csv")
    model = train(df_clean)

if __name__ == "__main__":
    run_pipeline()
