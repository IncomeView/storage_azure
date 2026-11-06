# src/storage_azure/pipelines/publish_dataset.py

from pathlib import Path
from storage_azure.datasets.metadata import (get_dataset, generate_metadata, save_metadata)
from storage_azure.database.postgres import (read_table)
from storage_azure.parquet.writer import (save_parquet)
from storage_azure.settings import (EXPORT_DIR)


def publish_dataset(dataset_name: str):
    dataset = get_dataset(dataset_name)

    if dataset is None:
        raise ValueError(
            f"Dataset '{dataset_name}' "
            f"não encontrado."
        )

    df = read_table(
        table=dataset["table"],
        schema=dataset["schema"],
    )

    parquet_file = (
        EXPORT_DIR
        / f"{dataset_name}.parquet"
    )

    save_parquet(df, parquet_file)
    metadata = generate_metadata(dataset_name, df)
    metadata_file = (
        EXPORT_DIR
        / f"{dataset_name}.metadata.json"
    )

    save_metadata(metadata, metadata_file)

    return {
        "dataset": dataset_name,
        "dataset_type": dataset["table"],
        "project": dataset["project"],
        "container": dataset["container"],
        "layer": dataset["layer"],
        "format": dataset["format"],
        "description": dataset["description"],
        "rows": len(df),
        "parquet_file": str(parquet_file),
        "metadata_file": str(metadata_file),
    }