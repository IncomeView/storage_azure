# tests/test_dataset_exists.py

from storage_azure.azure.containers import (dataset_exists)


if __name__ == "__main__":

    result = dataset_exists(
        dataset_name="ipca_geral",
        container="economics",
        layer="gold",
        project="inflation_bcb",
    )

    print(result)