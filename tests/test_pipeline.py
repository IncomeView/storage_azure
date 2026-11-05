# tests/test_pipeline.py

from storage_azure.pipelines.export_dataset import (export_dataset)


if __name__ == "__main__":
    file = export_dataset("ipca_geral")
    print(file)
