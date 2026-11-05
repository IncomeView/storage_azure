from storage_azure.datasets.registry import (DATASETS)
from storage_azure.pipelines.publish_dataset import (publish_dataset)


def publish_project(project_name: str):
    results = []
    for dataset_name, dataset in DATASETS.items():
        if (dataset["project"] != project_name):
            continue

        results.append(
            publish_dataset(dataset_name)
        )

    return results