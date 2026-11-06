# tests/test_publish_all_projects.py

from storage_azure.datasets.catalog import (list_projects)
from storage_azure.pipelines.publish_project import (publish_project)


if __name__ == "__main__":
    for project in list_projects():
        result = publish_project(project)

        print(
            f"{project}: "
            f"{len(result)} datasets publicados"
        )