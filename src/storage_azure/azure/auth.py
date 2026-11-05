# src/storage_azure/azure/auth.py

from azure.identity import (DefaultAzureCredential, ClientSecretCredential)
from dotenv import load_dotenv
import os

load_dotenv()


def get_credential():
    use_default = os.getenv(
        "AZURE_USE_DEFAULT_CREDENTIAL",
        "false"
    ).lower()

    if use_default == "true":
        return DefaultAzureCredential()

    return ClientSecretCredential(
        tenant_id=os.getenv("AZURE_TENANT_ID"),
        client_id=os.getenv("AZURE_CLIENT_ID"),
        client_secret=os.getenv("AZURE_CLIENT_SECRET"),
    )