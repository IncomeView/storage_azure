# src/storage_azure/pipelines/export_schema.py

from storage_azure.database.postgres import (list_tables)
from storage_azure.pipelines.export_dataset import (export_dataset)


def export_schema(schema: str = "bcb"):
    exported = []
    for table in list_tables(schema):
        result = export_dataset(
            table=table,
            schema=schema,
        )
        exported.append(result)

    return exported