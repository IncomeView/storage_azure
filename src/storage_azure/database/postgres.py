# src/publishing/database/postgres.py

from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()


def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    connection_string = (
        f"postgresql+psycopg2://"
        f"{user}:{password}"
        f"@{host}:{port}/{database}"
    )

    return create_engine(connection_string, pool_pre_ping=True)



def read_table(table: str, schema: str = "bcb"):
    query = f"""
    SELECT *
    FROM {schema}.{table}
    """

    return pd.read_sql(query, get_engine())



def list_tables(schema: str = "bcb"):
    query = f"""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = '{schema}'
    ORDER BY table_name
    """

    return pd.read_sql(query, get_engine())["table_name"].tolist()