# src/storage_azure/datasets/metadata.py

from storage_azure.datasets.registry import (DATASETS)

def get_dataset(name: str):
    return DATASETS.get(name)