# tests/test_upload_project.py

from storage_azure.azure.upload_project import (upload_project)


if __name__ == "__main__":
    result = upload_project("inflation_bcb")

    print(f"{len(result)} datasets enviados")

    for item in result:
        print(item)