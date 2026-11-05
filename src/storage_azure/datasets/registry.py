# src/storage_azure/datasets/registry.py


DATASETS = {

    "ipca_geral": {
        "schema": "bcb",
        "table": "ipca_geral",
        "description": "IPCA geral",
        "project": "inflation_bcb",
        "container": "economics",
        "layer": "gold",
        "format": "parquet",
    },
    "ipca_grupos": {
        "schema": "bcb",
        "table": "ipca_grupos",
        "description": "IPCA por grupos",
        "project": "inflation_bcb",
        "container": "economics",
        "layer": "gold",
        "format": "parquet",
    },
    "ipca_subgrupos": {
        "schema": "bcb",
        "table": "ipca_subgrupos",
        "description": "IPCA por subgrupos",
        "project": "inflation_bcb",
        "container": "economics",
        "layer": "gold",
        "format": "parquet",
    },
    "ipca_itens": {
        "schema": "bcb",
        "table": "ipca_itens",
        "description": "IPCA por itens",
        "project": "inflation_bcb",
        "container": "economics",
        "layer": "gold",
        "format": "parquet",
    },
    "ipca_subitens": {
        "schema": "bcb",
        "table": "ipca_subitens",
        "description": "IPCA por subitens",
        "project": "inflation_bcb",
        "container": "economics",
        "layer": "gold",
        "format": "parquet",
    },
}
