# etl/dashboard.py
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Database connection details (must match docker-compose)
DB_USER = "etl_user"
DB_PASS = "etl_pass"
DB_HOST = "db"
DB_PORT = "5432"
DB_NAME = "etl_db"

# Create connection
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

st.title("📊 Movies Dataset Dashboard")

@st.cache_data
def load_data():
    query = "SELECT * FROM movies"
    return pd.read_sql(query, engine)

df = load_data()

st.subheader(f"Total Records: {len(df)}")
st.dataframe(df.head(10))

st.subheader("Height Distribution")
st.bar_chart(df["height(inches)"])

st.subheader("Weight Distribution")
st.bar_chart(df["weight(pounds)"])
