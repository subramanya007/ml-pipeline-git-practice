# data_cleaning.py  (v2 - feature/data-cleaning branch)
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

EXPECTED_COLUMNS = ["age", "income",  "label"]

def load_data(path: str) -> pd.DataFrame:
    """Load raw CSV and validate expected columns exist."""
    df = pd.read_csv(path)
    logger.info(f"Loaded {len(df)} rows from {path}")
    return df

def validate_columns(df: pd.DataFrame, expected: list) -> None:
    """Raise an error if expected columns are missing."""
    missing = [c for c in expected if c not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Smarter null handling:
    - Numeric columns: fill with median (robust to outliers)
    - Drop rows only if label is missing (can't train without target)
    """
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    numeric_cols = [c for c in numeric_cols if c != "label"]

    for col in numeric_cols:
        median_val = df[col].median()
        nulls = df[col].isna().sum()
        if nulls > 0:
            df[col] = df[col].fillna(median_val)
            logger.info(f"Filled {nulls} nulls in '{col}' with median={median_val:.2f}")

    # Only drop rows if the target label is missing
    before = len(df)
    df = df.dropna(subset=["label"])
    dropped = before - len(df)
    if dropped:
        logger.warning(f"Dropped {dropped} rows with missing label")

    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows and report how many were removed."""
    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)
    if removed:
        logger.info(f"Removed {removed} duplicate rows")
    return df

def clip_outliers(df: pd.DataFrame, columns: list, lower=0.01, upper=0.99) -> pd.DataFrame:
    """Clip extreme values to 1st/99th percentile to reduce outlier impact."""
    for col in columns:
        low = df[col].quantile(lower)
        high = df[col].quantile(upper)
        df[col] = df[col].clip(low, high)
    logger.info(f"Clipped outliers in: {columns}")
    return df

def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Full cleaning pipeline."""
    validate_columns(df, EXPECTED_COLUMNS)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = clip_outliers(df, columns=["age", "income", "score"])
    logger.info(f"Cleaning complete. Final shape: {df.shape}")
    return df

def save(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False)
    logger.info(f"Saved cleaned data to {path}")

if __name__ == "__main__":
    df = load_data("data/raw.csv")
    df = clean(df)
    save(df, "data/clean.csv")
