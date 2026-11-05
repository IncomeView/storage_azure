# src/storage_azure/azure/upload.py

from pathlib import Path
from storage_azure.azure.adls import (get_adls_client)
from storage_azure.datasets.metadata import (get_dataset)
from storage_azure.datasets.path_builder import (build_dataset_path)



def upload_file(
    local_file: str | Path,
    remote_path: str,
):

    local_file = Path(local_file)
    client = get_adls_client()

    filesystem = client.get_file_system_client("economics")
    file_client = filesystem.get_file_client(remote_path)

    with open(
        local_file,
        "rb"
    ) as f:
        data = f.read()

    file_client.upload_data(
        data,
        overwrite=True,
    )

    return remote_path



def upload_dataset(dataset_name: str):
    dataset = get_dataset(dataset_name)

    if dataset is None:
        raise ValueError(
            f"Dataset '{dataset_name}' "
            "não encontrado."
        )

    dataset_path = build_dataset_path(dataset)
    parquet_file = Path(f"exports/{dataset_name}.parquet")
    metadata_file = Path(f"exports/{dataset_name}.metadata.json")

    client = get_adls_client()
    fs = client.get_file_system_client(dataset["container"])

    for local_file in [parquet_file, metadata_file]:

        remote_path = (
            f"{dataset_path}/"
            f"{local_file.name}"
        )
        file_client = (
            fs.get_file_client(remote_path)
        )
        with open(
            local_file,
            "rb",
        ) as f:
            file_client.upload_data(
                f.read(),
                overwrite=True,
            )

    return str(dataset_path)