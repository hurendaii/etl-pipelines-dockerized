import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "movies.csv"

def extract_data(file_path: Path) -> pd.DataFrame:
    """Read CSV data into a DataFrame."""
    return pd.read_csv(file_path)

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Simple transform: rename columns and filter rows."""
    df = df.rename(columns=lambda c: c.strip().lower().replace(" ", "_"))
    return df.head(10)  # just take 10 rows for demo

def load_data(df: pd.DataFrame):
    """For now, just print to stdout."""
    print(df)

def main():
    df = extract_data(DATA_FILE)
    df = transform_data(df)
    load_data(df)

if __name__ == "__main__":
    main()
