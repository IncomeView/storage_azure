# src/storage_azure/azure/containers.py

from storage_azure.azure.adls import (get_adls_client)


def list_containers():
    client = get_adls_client()
    return [
        item.name
        for item
        in client.list_file_systems()
    ]