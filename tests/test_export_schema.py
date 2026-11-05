# tests/test_export_schema.py

from storage_azure.pipelines.export_schema import (export_schema)


if __name__ == "__main__":
    files = export_schema()
    print(f"{len(files)} datasets exportados")