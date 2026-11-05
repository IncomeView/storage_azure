# tests/test_publish_dataset.py

from storage_azure.pipelines.publish_dataset import (publish_dataset)


if __name__ == "__main__":
    result = publish_dataset("ipca_geral")
    print(result)