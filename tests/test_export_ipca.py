from storage_azure.database.postgres import (read_table)
from storage_azure.parquet.writer import (save_parquet)


if __name__ == "__main__":
    df = read_table(
        table="ipca_geral",
        schema="bcb",
    )

    file = save_parquet(
        df,
        "exports/ipca_geral.parquet",
    )

    print(file)