# scripts/publish_project.py

import argparse
from storage_azure.pipelines.publish_project import (publish_project)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project",
        required=True,
        help="Project name",
    )

    args = parser.parse_args()
    result = publish_project(args.project)

    print(f"{len(result)} datasets publicados")

    for dataset in result:
        print(dataset)


if __name__ == "__main__":
    main()