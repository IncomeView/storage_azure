# src/storage_azure/pipelines/publish_dataset.py

from storage_azure.datasets.metadata import (get_dataset)
from storage_azure.pipelines.export_dataset import (export_dataset)


def publish_dataset(dataset_name: str,):
    dataset = get_dataset(dataset_name)

    if dataset is None:
        raise ValueError(
            f"Dataset '{dataset_name}' "
            f"não encontrado."
        )

    export_info = export_dataset(
        table=dataset["table"],
        schema=dataset["schema"],
    )

    return {

        "dataset": dataset_name,
        "project": dataset["project"],
        "container": dataset["container"],
        "layer": dataset["layer"],
        "format": dataset["format"],
        "description": dataset["description"],
        "export": export_info,
    }
