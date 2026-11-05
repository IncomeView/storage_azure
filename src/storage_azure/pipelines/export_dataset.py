# src/storage_azure/pipelines/export_dataset.py

from storage_azure.database.postgres import (read_table)
from storage_azure.parquet.writer import (save_parquet)
from storage_azure.settings import (EXPORT_DIR)


def export_dataset(
    table: str,
    schema: str = "bcb",
):

    df = read_table(
        table=table,
        schema=schema,
    )

    output_file = (f"{EXPORT_DIR}/{table}.parquet")

    save_parquet(
        df,
        output_file,
    )

    return {
        "table": table,
        "rows": len(df),
        "output_file": str(output_file),
    }