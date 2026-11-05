# src/storage_azure/datasets/catalog.py

from storage_azure.datasets.registry import (DATASETS)
from storage_azure.datasets.metadata import (get_dataset)


def list_datasets():
    return sorted(DATASETS.keys())


def list_projects():
    projects = set()
    for dataset in DATASETS.values():
        projects.add(dataset["project"])

    return sorted(projects)


def list_domains():
    domains = set()
    for dataset in DATASETS.values():
        domains.add(dataset["domain"])

    return sorted(domains)



def describe_dataset(dataset_name: str):
    dataset = get_dataset(dataset_name)

    if dataset is None:
        raise ValueError(
            f"Dataset '{dataset_name}' "
            "não encontrado."
        )

    return dataset