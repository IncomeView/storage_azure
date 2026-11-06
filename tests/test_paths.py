# tests/test_paths.py

from storage_azure.azure.containers import (list_paths)


if __name__ == "__main__":
    paths = list_paths("economics")

    for path in paths:
        print(path)