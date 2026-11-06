# tests/test_project_files.py

from storage_azure.azure.containers import (list_project_files)


if __name__ == "__main__":
    files = list_project_files(
        container="economics",
        layer="gold",
        project="inflation_bcb",
    )

    for file in files:
        print(file)