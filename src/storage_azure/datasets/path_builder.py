# src/storage_azure/datasets/path_builder.py

from pathlib import Path


def build_dataset_path(dataset: dict,):

    return Path(dataset["layer"]
                ) / Path(dataset["project"])