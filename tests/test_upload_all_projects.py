# tests/test_upload_all_projects.py

from storage_azure.datasets.catalog import (list_projects)
from storage_azure.azure.upload_project import (upload_project)


if __name__ == "__main__":
    for project in list_projects():
        result = upload_project(project)

        print(
            f"{project}: "
            f"{len(result)} datasets enviados"
        )