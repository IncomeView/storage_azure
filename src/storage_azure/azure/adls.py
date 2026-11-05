# src/storage_azure/azure/adls.py

from azure.storage.filedatalake import (DataLakeServiceClient)
from storage_azure.azure.auth import (get_credential)
import os


def get_adls_client():
    account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
    account_url = (
        f"https://{account_name}"
        ".dfs.core.windows.net"
    )

    return DataLakeServiceClient(
        account_url=account_url,
        credential=get_credential(),
    )
