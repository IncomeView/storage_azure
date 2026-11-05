# tests/test_azure_connection.py

from storage_azure.azure.adls import (get_adls_client)


if __name__ == "__main__":
    client = get_adls_client()
    print(client)