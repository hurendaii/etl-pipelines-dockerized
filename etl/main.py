import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

DATA_FILE = Path(__file__).parent.parent / "data" / "movies.csv"

DATABASE_URL = "postgresql+psycopg2://etl_user:etl_pass@db:5432/etl_db"

def extract_data(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path)

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns=lambda c: c.strip().lower().replace(" ", "_").replace('"', ''))
    return df.head(10)

def load_data(df: pd.DataFrame):
    engine = create_engine(DATABASE_URL)
    table_name = "movies"
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into '{table_name}' table.")

def main():
    df = extract_data(DATA_FILE)
    df = transform_data(df)
    load_data(df)

if __name__ == "__main__":
    main()
