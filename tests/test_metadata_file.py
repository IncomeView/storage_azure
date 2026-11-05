from storage_azure.database.postgres import (read_table)
from storage_azure.datasets.metadata import (generate_metadata, save_metadata)


if __name__ == "__main__":
    df = read_table(table="ipca_geral")
    metadata = generate_metadata(
        "ipca_geral",
        df,
    )

    file = save_metadata(
        metadata,
        "exports/ipca_geral.metadata.json",
    )

    print(file)