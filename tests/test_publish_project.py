from storage_azure.pipelines.publish_project import (publish_project)


if __name__ == "__main__":
    results = publish_project("inflation_bcb")

    print(f"{len(results)} datasets publicados")