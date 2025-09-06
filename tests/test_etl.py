import pandas as pd
from etl.main import extract_data, transform_data
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "movies.csv"


def test_transform_row_count():
    df = extract_data(DATA_FILE)
    transformed = transform_data(df)
    assert len(transformed) <= len(df)
