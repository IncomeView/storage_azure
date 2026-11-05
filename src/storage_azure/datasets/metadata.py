# src/storage_azure/datasets/metadata.py

from datetime import datetime
from storage_azure.datasets.registry import (DATASETS)
from pathlib import Path
import json



def get_dataset(name: str):
    return DATASETS.get(name)


def generate_metadata(dataset_name: str, dataframe):
    dataset = get_dataset(dataset_name)

    if dataset is None:
        raise ValueError(
            f"Dataset '{dataset_name}' "
            "não encontrado."
        )

    return {
        "dataset": dataset_name,
        "project": dataset["project"],
        "schema": dataset["schema"],
        "table": dataset["table"],
        "description": dataset["description"],
        "container": dataset["container"],
        "layer": dataset["layer"],
        "format": dataset["format"],
        "rows": len(dataframe),
        "columns": dataframe.shape[1],
        "column_names": list(dataframe.columns),
        "exported_at": (
            datetime.utcnow()
            .isoformat()
        ),
    }



def save_metadata(
    metadata: dict,
    output_file: str | Path,
):

    output_file = Path(output_file)
    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            metadata,
            f,
            indent=4,
            ensure_ascii=False,
        )

    return output_file