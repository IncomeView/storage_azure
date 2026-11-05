# tests/test_connection.py

from storage_azure.database.postgres import (
    list_tables
)

if __name__ == "__main__":
    df = list_tables()
    print(df.head())