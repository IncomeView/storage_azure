# tests/test_upload_dataset.py

from storage_azure.azure.upload import (upload_dataset)


if __name__ == "__main__":
    result = upload_dataset("ipca_geral")
    print(result)