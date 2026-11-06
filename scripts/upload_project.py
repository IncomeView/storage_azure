# scripts/upload_project.py

import argparse
from storage_azure.azure.upload_project import (upload_project)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project",
        required=True,
        help="Project name",
    )

    args = parser.parse_args()
    result = upload_project(args.project)

    print(f"{len(result)} datasets enviados")

    for dataset in result:
        print(dataset)


if __name__ == "__main__":
    main()