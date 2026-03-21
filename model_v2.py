# model.py  (v2 - feature/model-enhancement branch)
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def load_clean_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    logger.info(f"Loaded clean data: {df.shape}")
    return df

def split_features_target(df: pd.DataFrame, target_col="label"):
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    return X, y

def build_pipeline(model_type="random_forest") -> Pipeline:
    """
    Build a sklearn Pipeline with:
    - StandardScaler: normalizes features so scale doesn't dominate
    - Classifier: chosen by model_type
    """
    if model_type == "logistic":
        clf = LogisticRegression(max_iter=1000, C=0.5)
    elif model_type == "random_forest":
        clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    else:
        raise ValueError(f"Unknown model_type: {model_type}")

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", clf),
    ])
    return pipeline

def evaluate(pipeline: Pipeline, X_test, y_test) -> None:
    """Print detailed evaluation metrics."""
    y_pred = pipeline.predict(X_test)
    logger.info("\n" + classification_report(y_test, y_pred))
    logger.info(f"Confusion matrix:\n{confusion_matrix(y_test, y_pred)}")

def train(df: pd.DataFrame, model_type="random_forest") -> Pipeline:
    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = build_pipeline(model_type)

    # Cross-validation to get reliable performance estimate
    cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring="accuracy")
    logger.info(f"CV Accuracy: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

    # Final fit on full train set
    pipeline.fit(X_train, y_train)
    logger.info(f"Test Accuracy: {pipeline.score(X_test, y_test):.3f}")

    evaluate(pipeline, X_test, y_test)
    return pipeline

if __name__ == "__main__":
    df = load_clean_data("data/clean.csv")
    model = train(df, model_type="random_forest")
