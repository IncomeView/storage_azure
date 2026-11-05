# tests/test_upload_file.py

from storage_azure.azure.upload import (upload_file)


if __name__ == "__main__":
    result = upload_file(
        "exports/ipca_geral.parquet",
        "gold/inflation_bcb/ipca_geral.parquet",
    )

    print(result)