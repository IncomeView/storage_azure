# src/storage_azure/azure/upload_project.py

from storage_azure.datasets.registry import (DATASETS)
from storage_azure.azure.upload_dataset import (upload_dataset)


def upload_project(project_name: str):
    uploaded = []

    for dataset_name, dataset in DATASETS.items():
        if (dataset["project"] != project_name):
            continue

        result = upload_dataset(dataset_name)
        uploaded.append(
            {
                "dataset": dataset_name,
                "path": result,
            }
        )

    return uploaded