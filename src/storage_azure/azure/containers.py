# src/storage_azure/azure/containers.py

from storage_azure.azure.adls import (get_adls_client)


def list_containers():
    client = get_adls_client()
    return [
        item.name
        for item
        in client.list_file_systems()
    ]


def list_paths(container: str,):
    client = get_adls_client()

    filesystem = (
        client.get_file_system_client(container)
    )

    return sorted(
        [
            item.name
            for item in filesystem.get_paths()
        ]
    )



def list_project_files(
    container: str,
    layer: str,
    project: str,
):

    paths = list_paths(container)
    prefix = f"{layer}/{project}/"

    return sorted(
        [
            path
            for path in paths
            if path.startswith(prefix)
        ]
    )



def dataset_exists(
    dataset_name: str,
    container: str,
    layer: str,
    project: str,
):

    files = list_project_files(
        container=container,
        layer=layer,
        project=project,
    )

    parquet_file = f"{dataset_name}.parquet"
    metadata_file = f"{dataset_name}.metadata.json"

    parquet_exists = any(
        file.endswith(parquet_file)
        for file in files
    )
    metadata_exists = any(
        file.endswith(metadata_file)
        for file in files
    )

    return {
        "dataset": dataset_name,
        "parquet": parquet_exists,
        "metadata": metadata_exists,
        "published": (parquet_exists and metadata_exists),
    }